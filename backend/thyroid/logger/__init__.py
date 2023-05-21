import logging
import os
from datetime import datetime

from from_root import from_root

# Generating a unique log file name based on the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creating the logs directory path using the from_root and the generated log file name
logs_path = os.path.join(from_root(), "logs", LOG_FILE)

# Creating the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Creating the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configuring the logging module with the log file path, log level, and log message format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s : %(message)s",
)

# For testing purposes only
if __name__ == "__main__":
    logging.info("Logging has started....")
