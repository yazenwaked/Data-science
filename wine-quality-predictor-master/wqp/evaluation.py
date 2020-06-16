import numpy as np
import pandas as pd
from typing import Dict
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline
def compute_model_metrics(model: Pipeline, x: pd.DataFrame, y: pd.DataFrame) -> Dict[str, float]:
    """
    This function computes the performance metrics of a given model and returns them as a dictionary.
    :param model: The machine learning model, as a Scikit Learn pipeline.
    :param x: The features, as a Pandas DataFrame.
    :param y: The response data, as a Pandas DataFrame.
    :return: A dictionary, containing 3 key-values:
        - rmse: the root mean square error
        - mae: the mean absolute error
        - r2: the r2 score
    """
    predictions = model.predict(X=x)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)
    return dict(rmse=rmse, mae=mae, r2=r2)