from .base import BaseModel
from abc import ABC
import pandas as pd


class OutlierModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)

    def predict_score(self, data_input: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("predict_score method is not implemented")
