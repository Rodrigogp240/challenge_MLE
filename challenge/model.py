import pandas as pd
import numpy as np

from typing import Tuple, Union, List

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from .module.getMinDiff import get_min_diff
from .module.getPeriodDay import get_period_day
from .module.isHighSeason import is_high_season
import pickle


class DelayModel:

    def __init__(
        self
    ):
        self._model = None  # Model should be saved in this attribute.

    def preprocess(
        self,
        data: pd.DataFrame,
        target_column: str = None
    ) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """
        top_10_features = [
            "OPERA_Latin American Wings",
            "MES_7",
            "MES_10",
            "OPERA_Grupo LATAM",
            "MES_12",
            "TIPOVUELO_I",
            "MES_4",
            "MES_11",
            "OPERA_Sky Airline",
            "OPERA_Copa Air"
        ]
        data['period_day'] = data['Fecha-I'].apply(get_period_day)
        data['high_season'] = data['Fecha-I'].apply(is_high_season)
        data['min_diff'] = data.apply(get_min_diff, axis=1)
        threshold_in_minutes = 15
        data['delay'] = np.where(data['min_diff'] > threshold_in_minutes, 1, 0)

        features = pd.concat([
            pd.get_dummies(data['OPERA'], prefix='OPERA'),
            pd.get_dummies(data['TIPOVUELO'], prefix='TIPOVUELO'),
            pd.get_dummies(data['MES'], prefix='MES')],
            axis=1
        )
        features = features[top_10_features]

        if not target_column:
            return features
        
        target = data[target_column]
        return (features, target.to_frame())

    def fit(
        self,
        features: pd.DataFrame,
        target: pd.DataFrame
    ) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.DataFrame): target.
        """
        x_train, _, y_train, _ = train_test_split(features, target, test_size = 0.33, random_state = 42)
        n_y0 = 37298
        n_y1 = 8400
        class_weight={1: n_y0/len(y_train), 0: n_y1/len(y_train)}
        reg_model_2 = LogisticRegression(class_weight=class_weight)
        self._model = reg_model_2.fit(x_train, y_train)
        return None

    def predict(
        self,
        features: pd.DataFrame
    ) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.

        Returns:
            (List[int]): predicted targets.
        """
        if self._model is None:
            # the probles is with the test
            raise ValueError("Model has not been trained. Call 'fit' method first.")

        predictions = self._model.predict(features)

        # Convert predictions to a list of integers
        predicted_targets = list(map(int, predictions))

        return predicted_targets
    
    def importer(
        self,
    )-> None:
        if self._model is None:
            # the probles is with the test
            raise ValueError("Model has not been trained. Call 'fit' method first.")
        with open('trained_log_reg-0.1.0.pkl') as f:
            pickle.dump(self._model,f)
        return None

