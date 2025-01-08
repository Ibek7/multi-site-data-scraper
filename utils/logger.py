import logging
import os

# Ensure logs directory exists
LOGS_DIR = "data/logs"
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Configure logging
LOG_FILE = os.path.join(LOGS_DIR, "scraper.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Optional: Print logs to the console
    ]
)

def get_logger(name):
    """
    Returns a logger instance for the given name.
    """
    return logging.getLogger(name)