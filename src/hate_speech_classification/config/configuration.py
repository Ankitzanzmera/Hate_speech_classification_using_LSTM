from hate_speech_classification.constants import *
from hate_speech_classification.utils.common import create_directories,read_yaml
from hate_speech_classification.entity.config_entity import (DataIngestionConfig,
                                                            DataTransformationConfig,
                                                            ModelTrainerConfig,
                                                            ModelEvaluationCOnfig)
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

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        temp_config = self.config.model_trainer
        params = self.params

        model_trainer_config = ModelTrainerConfig(
            root_dir = temp_config.root_dir,
            cleaned_data = temp_config.cleaned_data,
            tokenizer_path = temp_config.tokenizer_path,
            model_path = temp_config.model_path,
            X_test_path = temp_config.X_test_path,
            y_test_path = temp_config.y_test_path,
            MAX_LEN = params.MAX_LEN,
            MAX_WORDS = params.MAX_WORDS,
            EPOCHS = params.EPOCHS,
            BATCH_SIZE = params.BATCH_SIZE,
            VALIDATION_SPLIT = params.VALIDATION_SPLIT,
            LOSS = params.LOSS,
            METRICS = params.METRICS,
            ACTIVATION = params.ACTIVATION
        )
        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationCOnfig:
        temp_config = self.config.model_evaluation
        params = self.params
        
        model_evaluation_config = ModelEvaluationCOnfig(
            root_dir = temp_config.root_dir,
            tokenizer_path = temp_config.tokenizer_path,
            model_path = temp_config.model_path,
            evaluation_file_path = temp_config.evaluation_file_path,
            X_test_path = temp_config.X_test_path,
            y_test_path = temp_config.y_test_path,
            MAX_LEN = params.MAX_LEN, 
        )
        return model_evaluation_config