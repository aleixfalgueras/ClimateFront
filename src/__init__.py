from src.config import DevelopmentConfig

import logging


config = DevelopmentConfig ()

logging.basicConfig (level = config.LOG_LEVEL)