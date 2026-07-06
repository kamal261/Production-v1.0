import os
from dotenv import load_dotenv

from core.config.config_service import ConfigService

load_dotenv()


class Env:

    _config = ConfigService().get()

    PROJECT_NAME = os.getenv(
        "PROJECT_NAME",
        _config.get("project_name", "SEO_AI_PLATFORM")
    )

    MODE = os.getenv(
        "MODE",
        _config.get("mode", "safe")
    )

    SITE_URL = os.getenv(
        "SITE_URL",
        _config.get("site_url", "")
    )

    WP_SITE = os.getenv(
        "WP_SITE",
        _config.get("wp_site", "")
    )

    WP_USERNAME = os.getenv(
        "WP_USERNAME",
        _config.get("wp_username", "")
    )

    WP_APP_PASSWORD = os.getenv(
        "WP_APP_PASSWORD",
        _config.get("wp_app_password", "")
    )

    GSC_TOKEN = os.getenv(
        "GSC_TOKEN",
        _config.get("gsc_token", "")
    )

    SERP_API_KEY = os.getenv(
        "SERP_API_KEY",
        _config.get("serp_api_key", "")
    )

    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        _config.get("openai_api_key", "")
    )

    OPENROUTER_API_KEY = os.getenv(
        "OPENROUTER_API_KEY",
        _config.get("openrouter_api_key", "")
    )

    NARA_API_KEY = os.getenv(
        "NARA_API_KEY",
        _config.get("nara_api_key", "")
    )

    OLLAMA_URL = os.getenv(
        "OLLAMA_URL",
        _config.get("ollama_url", "http://localhost:11434")
    )

    DEFAULT_MODEL = os.getenv(
        "DEFAULT_MODEL",
        _config.get("default_model", "gpt-4.1")
    )