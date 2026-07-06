import json
from pathlib import Path

from core.config.config_schema import ConfigSchema


class ConfigStore:

    def __init__(self):

        self.path = Path("config.json")

        if not self.path.exists():

            self.save(ConfigSchema.DEFAULT)

    def load(self):

        with open(self.path, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, data):

        with open(self.path, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )