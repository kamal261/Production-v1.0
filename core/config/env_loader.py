from typing import Any, Dict
from core.config.config_service import ConfigService

class Env:
    """
    Lazy loader for environment/config values. Avoids module-level side-effects
    during import time which can break test discovery.
    """
    _config: Dict[str, Any] = None

    @classmethod
    def load(cls):
        if cls._config is None:
            cls._config = ConfigService().get() or {}
        return cls._config

    @classmethod
    def get(cls, key: str, default=None):
        return cls.load().get(key, default)
