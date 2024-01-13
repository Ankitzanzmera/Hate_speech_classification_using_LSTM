import sys
from hate_speech_classification.utils.logger import logger
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.pipelines.pipeline_01_data_ingestion import DataIngestionPipeline
from hate_speech_classification.pipelines.pipeline_02_data_transformation import DataTransformationPipeline

STAGE_NAME = "Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("X"*80)
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