# utils/logger.py
import logging
import os

LOG_PATH = '/home/thriveni/Assignment/practiceAutomation/error.log'


import os
import logging

# Get current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Assume 'practiceAutomation' is a folder somewhere up in the hierarchy
# Let's find the base folder dynamically by searching upwards

def find_base_dir(target_folder_name):
    path = current_dir
    while True:
        if os.path.basename(path) == target_folder_name:
            return path
        parent = os.path.dirname(path)
        if parent == path:  # reached root directory
            raise FileNotFoundError(f"Folder '{target_folder_name}' not found in path hierarchy.")
        path = parent

try:
    base_path = find_base_dir('practiceAutomation')
except FileNotFoundError:
    base_path = current_dir  # fallback

log_file_path = os.path.join(base_path, 'error.log')




# Ensure directory exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

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
