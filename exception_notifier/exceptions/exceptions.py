class UnknownTargetNotifySource(Exception):
    """Notify source must be one of NotifySources values"""


class NotifySourceNotGiven(Exception):
    """set notify source name as global_exception_handler.init() param or set env var EXCEPTIONS_NOTIFY_TO"""


class ExampleError(Exception):
    """This is an example exception for test exception_notifier package"""

    def __init__(self):
        super().__init__(self.__doc__)


class FastApiInstanceNotGiven(Exception):
    def __init__(self):
        super().__init__('FastApi instance required')


class UnknownInstanceType(Exception):
    """instance type should be one of exception_notifier.utils.enums.InstanceTypes"""
