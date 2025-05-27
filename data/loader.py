import kagglehub
import pandas as pd
import os

def load_data():
    dataset_path = kagglehub.dataset_download("limtis/wikiliq-dataset")

    data_beer = pd.read_csv(os.path.join(dataset_path, "beer_data.csv"))
    data_spirits = pd.read_csv(os.path.join(dataset_path, "spirits_data.csv"))
    data_wine = pd.read_csv(os.path.join(dataset_path, "wine_data.csv"))
    
    return data_beer, data_spirits, data_wine

def extract_unique_values(data: pd.DataFrame, col: str):
    """
        Extracts unique, stripped values from a specified column in a pandas DataFrame,
        where each cell may contain comma-separated values.

        Args:
            data (pd.DataFrame): The DataFrame containing the data.
            col (str): The name of the column to extract unique values from.

        Returns:
            list: A list of unique, stripped values found in the specified column.

        Raises:
            ValueError: If the specified column does not exist in the DataFrame.
    """
    
    if col not in data.columns:
        raise ValueError(f"Data {data} does not have {col} column")
    else:
        return list({t.strip() for notes in data[col] for t in str(notes).split(',') if pd.notnull(notes)})