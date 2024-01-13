import sys
from hate_speech_classification.components.comp_2_data_transformation import DataTransformation
from hate_speech_classification.config.configuration import ConfigurationManager
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.utils.exception import CustomException

class DataTransformationPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.initiate_data_transformation()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = "Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
    except Exception as e:
        raise CustomException(e,sys)