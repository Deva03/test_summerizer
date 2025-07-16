from textSummarizer.entity import DataValidationConfig
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger
from textSummarizer.config.configuration import ConfigurationManager

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            Files_Status = data_validation.validate_all_files_exist()
            logger.info(f"Train, Test and Validation Files Status : {Files_Status}")
        except Exception as e:
            raise e