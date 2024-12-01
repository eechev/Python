import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
    level=logging.DEBUG,
    filename='./Chapter10/app.log')

# this is a simple example of a logger
# loggers are global, therefore you can use it anywhere in your project
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")