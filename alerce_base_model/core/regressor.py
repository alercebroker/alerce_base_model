from .base import BaseModel
from abc import ABC
import pandas as pd


class RegressorModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)

    def predict(self, data_input: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("predict method is not implemented")
