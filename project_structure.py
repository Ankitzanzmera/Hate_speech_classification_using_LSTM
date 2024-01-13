from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO)

project_name = "hate_speech_classification"

list_of_file = [
    ".github/workflows/.gitkeep",
    f"config/config.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/exception.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/templates/index.html",
    f"notebooks/trials.ipynb",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_file:
    filepath = Path(filepath)
    dirname,filename = os.path.split(filepath)
    
    if dirname != "":
        os.makedirs(dirname,exist_ok=True)
        logging.info(f"{dirname} Created Successfully")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"{filepath} Created Successfully")
    else:
        logging.info(f"{filepath} already exists")
