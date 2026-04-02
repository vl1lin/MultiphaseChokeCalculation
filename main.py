from utils.logger_config import setup_logger
setup_logger()

import logging

logger = logging.getLogger(__name__)
logger.info("Проверка info")
logger.error("проверка error")
logger.debug("проверка debug")
logger.info("коней проверка")
