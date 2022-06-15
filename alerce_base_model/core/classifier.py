from .base import BaseModel
from abc import ABC
import pandas as pd


class ClassifierModel(BaseModel, ABC):
    def __init__(self, path_to_model: str):
        super().__init__(path_to_model)

    def predict_proba(self, data_input: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("predict_proba method is not implemented")
