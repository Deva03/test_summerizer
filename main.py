from textSummarizer.pipeline.level01_DataIngestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

Level_name = "Data Ingestion Stage"
try:
    logger.info(f"===>>> {Level_name} Started <<<===")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<=== {Level_name} Completed ===>>>")
except Exception as e:
    logger.exception(e)
    raise e