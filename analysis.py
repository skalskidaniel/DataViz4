import kagglehub
import pandas as pd
import os

dataset_path = kagglehub.dataset_download("limtis/wikiliq-dataset")

data_beer = pd.read_csv(os.path.join(dataset_path, "beer_data.csv"))
data_spirits = pd.read_csv(os.path.join(dataset_path, "spirits_data.csv"))
data_wine = pd.read_csv(os.path.join(dataset_path, "wine_data.csv"))

print(data_beer.head())
print(data_spirits.head())
print(data_wine.head())