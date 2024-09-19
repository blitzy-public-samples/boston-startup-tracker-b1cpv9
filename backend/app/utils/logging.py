# Import required modules
from logging import getLogger, basicConfig, Formatter, StreamHandler
from sys import stdout

# Set up the logger
logger = getLogger(__name__)

# Create a stream handler that outputs to stdout
handler = StreamHandler(stdout)

# Define the log format
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Configure the handler with the formatter
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Set the logging level (adjust as needed)
logger.setLevel('INFO')

# Configure basic logging settings
basicConfig(
    level='INFO',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Example usage (can be removed in production)
if __name__ == '__main__':
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')