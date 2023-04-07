import pytest

from pyexception_notifier import init
from pyexception_notifier.exceptions.exceptions import ExampleError
from pyexception_notifier.utils.enums import InstanceTypes


def raise_error():
    raise ExampleError


def test_raise_local_error():
    init(instance_type=InstanceTypes.LOCAL.value)

    with pytest.raises(ExampleError) as exc:
        raise_error()

    assert exc.value.args[0] == 'This is an example exception for test exception_notifier package'
