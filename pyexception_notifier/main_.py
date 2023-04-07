import sys
from traceback import format_exception

from fastapi import Request

from pyexception_notifier.config import settings
from pyexception_notifier.exceptions.exceptions import UnknownTargetNotifySource, NotifySourceNotGiven, \
    FastApiInstanceNotGiven, UnknownInstanceType
from pyexception_notifier.notify_sources_clients.telegram.client import notify_to_telegram
from pyexception_notifier.utils.enums import TargetNotifySources, InstanceTypes
from pyexception_notifier.utils.exception_parsers import format_traceback


def exception_notify_telegram(exctype, value, tb):
    exception_trace = format_exception(exctype, value, tb)
    parsed_exception_traceback = format_traceback(exception_trace)
    notify_to_telegram(message=parsed_exception_traceback)

    raise exctype(value)


def init(notify_to: TargetNotifySources = None, instance_type: InstanceTypes = 'fastapi', **kwargs) -> None:
    if notify_to is None:
        if settings.NOTIFY_TO is None:
            raise NotifySourceNotGiven

    if instance_type == InstanceTypes.FASTAPI.value:
        app = kwargs.get('app')
        if app is None:
            raise FastApiInstanceNotGiven

        @app.middleware("http")
        async def errors_handling(request: Request, call_next):
            try:
                return await call_next(request)
            except Exception as exc:
                if settings.NOTIFY_TO == TargetNotifySources.TELEGRAM:
                    exception_notify_telegram(*sys.exc_info())
                else:
                    raise UnknownTargetNotifySource
                raise exc

        return

    if instance_type == InstanceTypes.LOCAL.value:
        sys.excepthook = exception_notify_telegram
        return

    raise UnknownInstanceType
