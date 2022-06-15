from .base import BaseModel
from abc import ABC, abstractmethod
import pandas as pd


class RegressorModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)

    @abstractmethod
    def predict(self, data_input: pd.DataFrame) -> pd.DataFrame:
        """
        Get the prediction of the data input.
        :param data_input: DataFrame of observations to predict.
        :return: DataFrame of predictions.
        """
