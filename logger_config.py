import logging
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler


def setup_logger():
    formatter = logging.Formatter('%(asctime)s — %(name)s — %(levelname)s — %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler('app.log', maxBytes=5*1024*1024, backupCount=3, encoding='utf-8')
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    if not root_logger.handlers:
        root_logger.addHandler(file_handler)
        root_logger.addHandler(stream_handler)

    return root_logger
