from core.logger import get_logger
from core.config.env_loader import Env


def bootstrap():

    logger = get_logger()

    logger.info("Starting SEO AI Platform")

    return {
        "name": Env.PROJECT_NAME,
        "mode": Env.MODE,
        "logger": logger
    }