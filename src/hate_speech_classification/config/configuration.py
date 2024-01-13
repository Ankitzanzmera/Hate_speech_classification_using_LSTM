from hate_speech_classification.constants import *
from hate_speech_classification.utils.common import create_directories,read_yaml
from hate_speech_classification.entity.config_entity import (DataIngestionConfig,
                                                            DataTransformationConfig)
class ConfigurationManager():
    def __init__(self,config_filepath = CONFIG_FILEPATH,params_filepath = PARAMS_FILEPATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        temp_config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir = temp_config.root_dir,
            source = temp_config.source,
            local_data_filepath = temp_config.local_data_filepath,
            unzip_dir = temp_config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        temp_config = self.config.data_transformation

        data_transformation_config = DataTransformationConfig(
            root_dir = temp_config.root_dir,
            data_path = temp_config.data_path,
            transformed_data_path = temp_config.transformed_data_path
        )
        return data_transformation_config