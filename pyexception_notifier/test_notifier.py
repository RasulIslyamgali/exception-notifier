from pyexception_notifier import init
from pyexception_notifier.exceptions.exceptions import ExampleError
from pyexception_notifier.utils.enums import InstanceTypes


init(instance_type=InstanceTypes.LOCAL.value)


def raise_error():
    raise ExampleError


raise_error()
