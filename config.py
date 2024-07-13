import logging


def setup_logging():
    # Create a root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # File handler - only logs errors and critical messages
    error_file_handler = logging.FileHandler("error.log")
    error_file_handler.setLevel(logging.ERROR)
    error_file_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    error_file_handler.setFormatter(error_file_formatter)
    logger.addHandler(error_file_handler)

    # File handler - only logs info messages
    info_file_handler = logging.FileHandler("app.log")
    info_file_handler.setLevel(logging.INFO)
    info_file_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    info_file_handler.setFormatter(info_file_formatter)
    info_file_handler.addFilter(lambda record: record.levelno == logging.INFO)
    logger.addHandler(info_file_handler)

    # Console handler - logs all messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    return logger
