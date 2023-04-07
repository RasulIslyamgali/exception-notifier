from enum import Enum


class TargetNotifySources(Enum):
    TELEGRAM: str = 'telegram'


class InstanceTypes(Enum):
    FASTAPI: str = 'fastapi'
    LOCAL: str = 'local'
