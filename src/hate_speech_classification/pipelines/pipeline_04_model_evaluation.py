import sys
from hate_speech_classification.config.configuration import ConfigurationManager
from hate_speech_classification.components.comp_4_model_evaluation import ModelEvaluation
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.logger import logger

class ModelEvaluationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.initiate_model_evaluation()
        except Exception as e:
            raise CustomException(e,sys)


STAGE_NAME = "Model Evaluation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)