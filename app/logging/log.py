import copy
import logging

from common.colors import yellow, red, cyan, green


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