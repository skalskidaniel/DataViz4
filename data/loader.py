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
        data = pd.read_csv("data/beer_data.csv",  index_col=0)
    elif type.lower() == 'wine':
        data = pd.read_csv("data/wine_data.csv", index_col=0)
    elif type.lower() == 'spirits':
        data = pd.read_csv("data/spirits_data.csv", index_col=0)
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
        return sorted(list({t.strip() for i in data[col] for t in str(i).split(',') if pd.notnull(i)}))
    
def extract_item_value(item: pd.Series, col: str):
    """
    Extracts and returns a sorted list of unique, stripped values from a specified column in a pandas Series.
    Parameters:
        item (pd.Series): The pandas Series from which to extract values.
        col (str): The name of the column to extract values from.
    Returns:
        list: A sorted list of unique, stripped values from the specified column. 
              If the column does not exist, returns ["Not available"].
    Notes:
        - Values in the column are expected to be comma-separated strings.
        - Null values are ignored.
    """
    
    if col not in item.index or not pd.notnull(item[col]):
        return ["Not available"]
    else:
        return sorted(list({i.strip() for i in str(item[col]).split(',')}))