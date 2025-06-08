"""import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH
    format="[%(asctime)s]%(lineno)d%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,



)"""

import logging
import os
from datetime import datetime

# Create log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory path (corrected variable name from 'logs_path' to 'log_path')
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_path, exist_ok=True)  # Corrected variable name here

# Full path for the log file (corrected variable name)
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Added missing comma
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Added spaces for better readability
    level=logging.INFO
)  # Removed extra comma


if __name__=="__main__":
    logging.info("Logging has started")



## Recommended Version
"""
import logging 
import os
from datetime import datetime

# Configure logging
def setup_logging():
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)
    
    # Create log file with timestamp
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
    
    # Basic configuration
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(levelname)s @ %(name)s:%(lineno)d - %(message)s",
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'  # Added date format for better readability
    )
    
    # Also log to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

# Initialize logging
setup_logging()"""