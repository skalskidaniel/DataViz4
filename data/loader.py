import pandas as pd
import numpy as np

def load_data(type: str) -> pd.DataFrame:
    """
        Loads data from csv file and updates column types:
        - Numeric columns are converted to float.
        - Comma-separated string columns are converted to lists.
        
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


from typing import Tuple

def query_data(data: pd.DataFrame, category: str, taste: list[str], food: list[str], price_range: list[int]) -> Tuple[pd.DataFrame, pd.Series]:
    """
        Parameters:
            data (pd.DataFrame): The input DataFrame containing food or beverage items with columns such as "Categories", "Tasting Notes", "Food Pairing", "Price", and "Rating".
            category (str): The category to filter by. If empty, no category filtering is applied.
            taste (list[str]): A list of tasting notes to filter by. Each note must be present in the item's "Tasting Notes".
            food (list[str]): A list of food pairings to filter by. Each food must be present in the item's "Food Pairing".
            price_range (list[int]): A two-element list specifying the minimum and maximum price (inclusive) to filter by.
        Returns:
            Tuple[pd.DataFrame, pd.Series]:
                - pd.DataFrame: A DataFrame containing the top 10 filtered items with columns ["No", "Name", "Price", "Rating"], sorted by "Rating" in descending order.
                - pd.Series: The row (as a Series) of the top-rated item after filtering.
        Raises:
            ValueError: If price_range is not a two-element list.
    """
    cols = ["Name", "Price", "Rating"]
    
    df = data.copy()

    if category:
        df = df[df["Categories"].apply(lambda x: category in (x if isinstance(x, list) else str(x).split(',')))]

    if taste:
        for t in taste:
            df = df[df["Tasting Notes"].apply(lambda x: t in (x if isinstance(x, list) else str(x).split(',')))]

    if food:
        for f in food:
            df = df[df["Food Pairing"].apply(lambda x: f in (x if isinstance(x, list) else str(x).split(',')))]

    if len(price_range) != 2:
        raise ValueError("price_range must be a two-element list")
    
    if 'Price' in df.columns:
        df["Price_numeric"] = df["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
        df["Price_numeric"] = pd.to_numeric(df["Price_numeric"], errors="coerce")
        
        df = df[(df["Price_numeric"] >= price_range[0]) & (df["Price_numeric"] <= price_range[1])]
        
        df = df.drop('Price_numeric', axis=1)
        
    top_item = df.sort_values(by=["Rating", "Price"], ascending=[False, True]).iloc[0]
        
    df = df[cols].sort_values(by=["Rating", "Price"], ascending=[False, True]).head(10)
    df = df.reset_index(drop=True)
    df["No"] = df.index + 1

    return df[["No", "Name", "Price", "Rating"]], top_item