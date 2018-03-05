import copy
import logging
import logging.config
import os
import yaml

from app.log.colors import yellow, red, green


class ConsoleHandler(logging.StreamHandler):
    """Logging to console handler."""

    def emit(self, record):
        colored = copy.copy(record)
        if record.levelname == "INFO":
            colored.msg = yellow(record.msg)
        elif record.levelname == "ERROR" or record.levelname == "CRITICAL":
            colored.msg = red(record.msg)
        elif record.levelname == "DEBUG":
            colored.msg = green(record.msg)

        logging.StreamHandler.emit(self, colored)


def setup_logging(
        default_path='app/log/logging.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration

        """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level, format=' %(asctime)s - %(name)s -%(levelname)s - %(message)s')



