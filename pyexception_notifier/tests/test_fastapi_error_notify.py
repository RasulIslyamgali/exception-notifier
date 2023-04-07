import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient

from pyexception_notifier.config import settings
from pyexception_notifier.utils.enums import TargetNotifySources

app = FastAPI()


@app.get('/error')
async def root():
    zero_division_error = 1 / 0


client = TestClient(app)


def test_notify_error_to_telegram():
    if settings.NOTIFY_TO == TargetNotifySources.TELEGRAM.value:
        with pytest.raises(ZeroDivisionError) as exc:
            response = client.get('/error')
            assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR

        assert exc.value.args[0] == 'some'
    assert True
