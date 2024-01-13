from pathlib import Path
import sys,os
from ensure import ensure_annotations
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from typing import Any
from hate_speech_classification.utils.exception import CustomException

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        with open(path_to_yaml,"r") as yaml_file:
            content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def create_directories(list_of_directory: list):
    try:
        for path in list_of_directory:
            os.makedirs(path,exist_ok= True)
    except Exception as e:
        raise CustomException(e,sys)