from mlProject import logger
from mlProject.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")

except Exception as e:
        logger.exception(e)
        raise e
