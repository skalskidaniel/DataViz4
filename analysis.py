import kagglehub

# data = kagglehub.dataset_download("limtis/wikiliq-dataset")

data = kagglehub.load_dataset(kagglehub.KaggleDatasetAdapter.PANDAS, "limtis/wikiliq-dataset", "beer_data.csv")

print(data)