from exception_notifier import init
from exception_notifier.exceptions.exceptions import ExampleError
from exception_notifier.utils.enums import InstanceTypes


init(instance_type=InstanceTypes.LOCAL.value)


def raise_error():
    raise ExampleError


raise_error()
