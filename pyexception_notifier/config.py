from pathlib import Path

from pydantic import BaseSettings, root_validator

from pyexception_notifier.utils.enums import TargetNotifySources


class Settings(BaseSettings):
    NOTIFY_TO: TargetNotifySources = None
    BOT_TOKEN: str = None
    CHAT_ID: str = None
    SERVICE_NAME: str = None

    class Config:
        env_file = Path(__file__).parent.parent / '.env'
        env_prefix = 'EXCEPTION_NOTIFY_'

    @root_validator
    def root_validator_(cls, values):
        if not all((values['BOT_TOKEN'], values['CHAT_ID'], values['SERVICE_NAME'], values['NOTIFY_TO'])):
            raise ValueError(f"please set env vars for exception notifier package {values}")
        return values


settings = Settings()
