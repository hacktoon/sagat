import logging
from io import StringIO
from saga import formatter

class Log:
    def __init__(self, runtime, traceid, log_level):
        level = logging.getLevelName(log_level)
        # Task log message
        self.str_stream = StringIO()
        self.runtime = runtime
        # Create and configure a basic logger
        # Use specific task name and id for each task runtime
        self._logger = logging.getLogger(f'{runtime.name}:{traceid}')
        # Set base logger level
        self._logger.setLevel(level)
        # Avoid duplicating logs on parent logger, use child only
        self._logger.propagate = False
        # create log formatter
        formatter_obj = formatter(runtime, traceid)
        # Create console handler
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter_obj)
        self._logger.addHandler(stdout_handler)
        # Create string handler
        string_handler = logging.StreamHandler(self.str_stream)
        string_handler.setLevel(level)
        string_handler.setFormatter(formatter_obj)
        self._logger.addHandler(string_handler)

    @property
    def message(self):
        return self.str_stream.getvalue()

    def debug(self, message):
        return self._logger.debug(self._fmt_error(message))

    def info(self, message):
        return self._logger.info(message)

    def warning(self, message):
        return self._logger.warning(message)

    def error(self, message):
        return self._logger.error(self._fmt_error(message))

    def critical(self, message):
        self._logger.critical(self._fmt_error(message))

    def _fmt_error(self, message):
        return f'{message} {self.runtime.result}'
