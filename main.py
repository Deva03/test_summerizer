from textSummarizer.pipeline.level01_DataIngestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.level02_DataValidation import DataValidationTrainingPipeline
from textSummarizer.pipeline.level03_DataTransformation import DataTransformationTrainingPipeline

Level1_name = "Data Ingestion Stage"
try:
    logger.info(f"===>>> {Level1_name} Started <<<===")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"<<<=== {Level1_name} Completed ===>>>")
except Exception as e:
    logger.exception(e)
    raise e


Level2_name = "Data Validation Stage"
try:
    logger.info(f"===>>> {Level2_name} Started <<<===")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"<<<=== {Level2_name} Completed ===>>>")
except Exception as e:
    logger.exception(e)
    raise e


Level3_name = "Data Transformation Stage"
try:
    logger.info(f"===>>> {Level3_name} Started <<<===")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f"<<<=== {Level3_name} Completed ===>>>")
except Exception as e:
    logger.exception(e)
    raise e