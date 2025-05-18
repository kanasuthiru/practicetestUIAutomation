# utils/logger.py
import logging
import os

LOG_PATH = '/home/thriveni/Assignment/practiceAutomation/error.log'

# Ensure directory exists
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Clear existing handlers
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=LOG_PATH,
    filemode='a'
)

def setup_logging():
    logger = logging.getLogger(__name__)
    return logger
