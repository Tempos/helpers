import logging


def logger_call(log_file_name):
    """ Configure logger """

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s -- %(module)s -- %(levelname)s -- %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S')

    # Save log to file
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Show log in console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
