from abc import abstractmethod

import pandas as pd


class BaseModel:
    def __init__(self, path_to_model: str):
        self.model = None
        self._load_model(path_to_model)

    @abstractmethod
    def _load_model(self, path_to_model: str) -> None:
        """
        Private method to load your model in memory. For example in torch models, you can use torch.load() for load
        the model.

        :param path_to_model: string of the path
        :return: None
        """

    @abstractmethod
    def preprocess(self, data_input: pd.DataFrame) -> pd.DataFrame:
        """
        Method for preprocess input data. You need to implement transformation, filters or custom processes to
        preprocess the data.

        :param data_input: DataFrame with input data
        :return: DataFrame of preprocessed input data
        """
