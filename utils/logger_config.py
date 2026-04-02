import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_log_dir() -> Path:
    if getattr(sys, 'frozen', False):
        base_path = Path(sys.executable).parent
    else:
        base_path = Path(__file__).parent
    log_dir = base_path / "logs"
    log_dir.mkdir(exist_ok=True)
    return log_dir / "app.log"


def setup_logger():
    formatter = logging.Formatter('%(asctime)s — %(name)s — %(levelname)s — %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    if root_logger.handlers:
        return

    file_handler = RotatingFileHandler(get_log_dir(), maxBytes=5*1024*1024, backupCount=3, encoding='utf-8')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
