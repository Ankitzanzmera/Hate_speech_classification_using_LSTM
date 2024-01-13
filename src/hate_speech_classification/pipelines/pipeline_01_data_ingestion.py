import sys
from hate_speech_classification.config.configuration import ConfigurationManager
from hate_speech_classification.components.comp_1_data_ingestion import DataIngestion
from hate_speech_classification.utils.exception import CustomException
from hate_speech_classification.utils.logger import logger

class DataIngestionPipeline:
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_file()
        except Exception as e:
            raise CustomException(e,sys)
        

STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)