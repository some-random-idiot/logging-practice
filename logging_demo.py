"""
Examples of using Python's logging facility.

Run the file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging


def logging_test(logger):
    """Log messages using each of the standard logging levels 
       plus 1 custom log level.
    """
    level = logging.WARN + 5  # custom log level
    logger.debug("Player took 120 damage.")
    logger.info("Server started at 22:00 11/1/2021")
    logger.warning("No gender information provided. Calories calculations may be inaccurate.")
    logger.log(level, "This is a message of a custom log level")
    logger.error("Operator '+' can't be used with variables of bool type")
    logger.critical("Server shutdown unexpectedly: 'EXCEPTION_ACCESS_VIOLATION'")


def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You should call this before creating any logging objects.
    You can call basicConfig only once. 

    Some named attributes you can set using basicConfig are:

        filename = "name of a file to send log messages to"
        filemode = 'a' (append), 'w' (truncate & open for writing)
        format = a string describing format of log messages
        stream = name of a StreamHandler to use, cannot use with filename attribute
        level = the root logger level (threshold level for log msgs)

    See:  help(logging.basicConfig)
    https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # use a custom format for log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)


def my_config():
    """Write your own logging configuration."""
    formatting = "[%(asctime)s | %(name)s | %(levelname)s]: %(message)s"
    logging.basicConfig(format=formatting, level=logging.DEBUG, filename="log", filemode='w')


if __name__ == "__main__":
    # logging.basicConfig()
    # simple_config()
    my_config()

    # Log some messages to the root logger using different logging levels.
    logger = logging.getLogger()
    logger.setLevel(logging.WARN)
    print("Logging to ", str(logger))
    logging_test(logger)

    # Logging for the 'foo' module
    my_logger = logging.getLogger("foo")
    my_logger.setLevel(logging.DEBUG)  # log everything
    logging_test(my_logger)
