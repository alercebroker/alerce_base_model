from .base import BaseModel
from abc import ABC, abstractmethod
import pandas as pd


class OutlierModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)

    @abstractmethod
    def predict_score(self, data_input: pd.DataFrame) -> pd.DataFrame:
        """
        Get the prediction's scores of the data input. The index must be the identifier of each data_input
        (generally is the index of data_input).
        :param data_input: DataFrame of observations to predict.
        :return: DataFrame of scores.
        """
