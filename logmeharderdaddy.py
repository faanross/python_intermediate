# built-in features to add logging to our applications
import logging

# there are 5 different log levels we can log to
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# If we were to run these: only the last 3 will output to console
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# we can change basic settings of logging with basicConfig

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s  - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

# we can also create our own modules 
logger = logging.getLogger(__name__)
# now we can actually log something
logger.info('Hello, this is being logged')