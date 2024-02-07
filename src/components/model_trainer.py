import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from.src.utils.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    pass

class ModelTrainer:
    def __init__(self):
        pass

    def initiate_model_traning(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)


