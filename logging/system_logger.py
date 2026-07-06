from loguru import logger


class SystemLogger:

    def info(self, msg):

        logger.info(msg)

    def error(self, msg):

        logger.error(msg)

    def debug(self, msg):

        logger.debug(msg)