from fileinput import filename
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')



pckage_name="deepClaffier"


list_of_files = [ 
    ".github/workflow/.gitkeep",
    f"src/{pckage_name}/__init__.py",
    f"src/{pckage_name}/components/__init__.py",
    f"src/{pckage_name}/utils/__init__.py",
    f"src/{pckage_name}/config/__init__.py",
    f"src/{pckage_name}/pipeline/__init__.py",
    f"src/{pckage_name}/entity/__init__.py",
    f"src/{pckage_name}/constants/__init__.py",
    
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trails.ipynb"


]
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!=" ":
        os.makedirs(filedir,exist_ok=True)
        logging.info()
        