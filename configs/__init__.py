# This file marks the directory as a Python module


import yaml
import os
from utils.logger import get_logger

logger = get_logger(__name__)  # Initialize logger for this module

# Path to the YAML file
config_file = os.path.join(os.path.dirname(__file__), "academic.yaml")

try:
    # Load the YAML configuration
    with open(config_file, "r") as file:
        academic_configs = yaml.safe_load(file)
        logger.info("Successfully loaded academic configurations.")
        logger.debug(f"Academic Configurations: {academic_configs}")
except FileNotFoundError:
    logger.error(f"Configuration file not found: {config_file}")
    academic_configs = {}
except yaml.YAMLError as e:
    logger.error(f"Error parsing YAML file {config_file}: {e}")
    academic_configs = {}

# Expose configurations for each platform
pubmed = academic_configs.get("pubmed", {})
google_scholar = academic_configs.get("google_scholar", {})
ssrn = academic_configs.get("ssrn", {})

# Log specific configurations to verify they are loaded correctly
logger.debug(f"PubMed Config: {pubmed}")
logger.debug(f"Google Scholar Config: {google_scholar}")
logger.debug(f"SSRN Config: {ssrn}")