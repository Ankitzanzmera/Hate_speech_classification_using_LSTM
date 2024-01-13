import os,sys
from urllib.request import urlretrieve
from zipfile import ZipFile
from hate_speech_classification.entity.config_entity import DataIngestionConfig
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.utils.common import create_directories

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config
        create_directories([self.config.root_dir])

    def download_data(self):
        try:
            if not os.path.exists(self.config.local_data_filepath):
                filename,header = urlretrieve(self.config.source,self.config.local_data_filepath)
                logger.info("Zip File Downloaded Successfully")
            else:
                logger.info("Zip File Already Existed")
        except Exception as e:
            raise CustomException(e,sys)
        
    def extract_file(self):
        try:
            if not os.path.exists(self.config.unzip_dir):
                with ZipFile(self.config.local_data_filepath,"r") as zip_ref:
                    zip_ref.extractall(self.config.unzip_dir)
                logger.info("Zip file Extracted Successfully")
            else:
                logger.info("Zip file is Already Extracted")
        except Exception as e:
            raise CustomException(e,sys)
