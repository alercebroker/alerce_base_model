import pandas as pd


class BaseModel:
    def __init__(self, path_to_model: str):
        self.model = None
        self._load_model(path_to_model)

    def _load_model(self, path_to_model: str) -> None:
        raise NotImplementedError("load_model method is not implemented")

    def preprocess(self, data_input: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("preprocess method is not implemented")
