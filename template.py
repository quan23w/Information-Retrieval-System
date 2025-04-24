import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
list_file = [
    f"src/__init__.py",
    f"src/helpers.py",
    ".env",
    "reuqirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]
for filemane in list_file:
    filepath = Path(filemane)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Create directory: {filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Create empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")