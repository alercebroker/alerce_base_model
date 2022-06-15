from .base import BaseModel
from abc import ABC, abstractmethod
import pandas as pd


class ClassifierModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)
        self.taxonomy = None

    @abstractmethod
    def predict_proba(self, data_input: pd.DataFrame) -> pd.DataFrame:
        """
        Get the prediction's probabilities of the data input. The format of the output must be a column for
        each class in taxonomy. The index must be the identifier of each data_input (generally is the index).
        :param data_input: DataFrame of observations to predict.
        :return: DataFrame of probabilities. Each row is an observation and each column is probability of be a
         taxonomy class.
        """
