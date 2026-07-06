import json
import logging
from pathlib import Path

log = logging.getLogger(__name__)

class ConfigStore:
    def __init__(self, path: str = "core/config/config.json"):
        self.path = Path(path)

    def load(self):
        """
        Load JSON config from disk. If file is missing or invalid JSON,
        return an empty dict and log a warning. Do not raise to avoid
        breaking imports during test discovery.
        """
        if not self.path.exists():
            log.warning("Config file %s not found; returning empty config.", self.path)
            return {}

        try:
            with self.path.open("r", encoding="utf-8") as f:
                # read and strip to detect empty files
                content = f.read().strip()
                if not content:
                    log.warning("Config file %s is empty; returning empty config.", self.path)
                    return {}
                return json.loads(content)
        except json.JSONDecodeError as e:
            log.warning("Invalid JSON in config file %s: %s; returning empty config.", self.path, e)
            return {}
        except Exception as e:
            log.exception("Unexpected error loading config file %s: %s", self.path, e)
            return {}
