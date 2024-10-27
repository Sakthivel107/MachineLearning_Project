import logging
import os
from datetime import datetime

# Replace slashes with underscores for a valid filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
   filename=LOG_FILE_PATH,
   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
   level=logging.INFO,
)


