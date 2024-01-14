import sys
from hate_speech_classification.config.configuration import ConfigurationManager
from hate_speech_classification.components.comp_3_model_trainer import ModelTrainer
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.utils.exception import CustomException


class ModelTrainerPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.initiate_model_trainer()
        except Exception as e:
            raise CustomException(e,sys)


STAGE_NAME = "Model Trainer"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)
