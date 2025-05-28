import pandas as pd

def load_data(type: str) -> pd.DataFrame:
    """
        Loads data from csv file
        
        Args:
        type (str): [beer, wine, spirits]

        Returns:
            data: pandas DataFrame
    """
    
    data = None
    if type.lower() == 'beer':
        data = pd.read_csv("data/beer_data.csv")
    elif type.lower() == 'wine':
        data = pd.read_csv("data/wine_data.csv")
    elif type.lower() == 'spirits':
        data = pd.read_csv("data/spirits_data.csv")
    else:
        raise ValueError(f"Cannot find data for {type}")
    
    return data

def extract_unique_values(data: pd.DataFrame, col: str) -> list:
    """
        Extracts unique, stripped values from a specified column in a pandas DataFrame,
        where each cell may contain comma-separated values.

        Args:
            data (pd.DataFrame): The DataFrame containing the data.
            col (str): The name of the column to extract unique values from.

        Returns:
            list: A sorted list of unique, stripped values found in the specified column.

        Raises:
            ValueError: If the specified column does not exist in the DataFrame.
    """
    
    if col not in data.columns:
        raise ValueError(f"Data {data} does not have {col} column")
    else:
        return sorted(list({t.strip() for notes in data[col] for t in str(notes).split(',') if pd.notnull(notes)}))