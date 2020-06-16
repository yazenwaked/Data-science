from sklearn.model_selection import train_test_split
from typing import Optional, Tuple, Dict
import pandas as pd
def fetch_csv_data(url: str, separator: Optional[str]) -> pd.DataFrame:
    """
    This functions fetch the CSV data from a given path (or url) and returns a Pandas DataFrame.
    :param url: a string containing the address of the data (local path, url ...)
    :param separator: an optional separator to override the default separator (comma)
    :return: a Pandas Dataframe containing the loaded data
    """
    try:
        args = dict(filepath_or_buffer=url)
        if separator:
            args.update(sep=separator)
        return pd.read_csv(**args)
    except Exception as e:
        raise Exception(f'Error while fetching data at url {url}: {e}')
def build_train_test_sets(data: pd.DataFrame, label_col: str, train_size: float) -> \
        Dict[str, Tuple[pd.DataFrame, pd.DataFrame]]:
    """
    A function to split the data into training and test sets.
    :param data: a pandas dataframe
    :param label_col: the label column name
    :param train_size: float. The fraction of the whole dataset used for training.
    :return: a Dictionary of key (string) - value (tuple of pandas dataframes) containing training and test data.
    Dictionary keys:
        - train: contains (train_x, train_y)
        - test: contains (test_x, test_y
    """
    try:
        train, test = train_test_split(data, train_size=train_size)
        x_y = lambda _data: (_data.drop([label_col], axis=1), _data[[label_col]])
        train_x, train_y = x_y(train)
        test_x, test_y = x_y(test)
        return dict(train=(train_x, train_y), test=(test_x, test_y))
    except Exception as e:
        raise Exception(f'Error while splitting data: {e}')