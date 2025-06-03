import pandas as pd
import math

class Loader:
    def __init__(self) -> None:
        self.data = pd.DataFrame()
        self.load_data('beer')
        
    def load_data(self, type: str):

        if type.lower() == 'beer':
            self.data = pd.read_csv("data/beer_data.csv",  index_col=0)
        elif type.lower() == 'wine':
            self.data = pd.read_csv("data/wine_data.csv", index_col=0)
        elif type.lower() == 'spirits':
            self.data = pd.read_csv("data/spirits_data.csv", index_col=0)
        else:
            self.data = pd.DataFrame()
            raise ValueError(f"Cannot find data for {type}")
        
    def get_data(self):
        self.compute_score()
        
        return self.data

    def extract_unique_values(self, col: str) -> list:

        if col not in self.data.columns:
            return []
        else:
            return sorted(list({t.strip() for i in self.data[col] for t in str(i).split(',') if pd.notnull(i)}))
        
    def extract_price_range(self):
        self.data["Price_numeric"] = self.data["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
        self.data["Price_numeric"] = pd.to_numeric(self.data["Price_numeric"], errors="coerce")
        
        price_series = self.data["Price_numeric"].dropna()
        if price_series.empty:
            min_price, max_price = 0, 0
        else:
            min_price, max_price = price_series.min(), price_series.max()
        
        self.data = self.data.drop('Price_numeric', axis=1)
        
        return min_price, max_price
    
    def get_price_marks(self):
        max_price = self.extract_price_range()[1]
        max_price = int(math.ceil(max_price / 10.0)) * 10
        step = int(max_price / 5) if max_price >= 5 else 1
        marks = {i: f"${i}" for i in range(0, max_price, step)}
        marks[max_price] = f"${max_price}"
        
        return marks
        
    def extract_options_for_sidebar(self):
        cols = ["Categories", "Country", "Tasting Notes", "Food Pairing"]
        
        o1 = self.extract_unique_values(cols[0])
        o2 = self.extract_unique_values(cols[1])
        o3 = self.extract_unique_values(cols[2])
        o4 = self.extract_unique_values(cols[3])
        o5 = math.ceil(self.extract_price_range()[1] / 10.0) * 10
        o6 = self.get_price_marks()
        
        return o1, o2, o3, o4, o5, o6, [0, o5]
        
        
    def extract_item_value(self, item: pd.Series, col: str):

        if col not in item.index or not pd.notnull(item[col]):
            return ["Not available"]
        else:
            return sorted(list({i.strip() for i in str(item[col]).split(',')}))


    def filter_items(self, category: str, country: str, taste: list[str], food: list[str], price_range: list[int]):

        if category:
            self.data = self.data[self.data["Categories"].apply(lambda x: category in (x if isinstance(x, list) else str(x).split(',')))]

        if country:
            self.data = self.data[self.data["Country"].apply(lambda x: country in (x if isinstance(x, list) else str(x).split(',')))]
            
        if taste:
            for t in taste:
                self.data = self.data[self.data["Tasting Notes"].apply(lambda x: t in (x if isinstance(x, list) else str(x).split(',')))]

        if food:
            for f in food:
                self.data = self.data[self.data["Food Pairing"].apply(lambda x: f in (x if isinstance(x, list) else str(x).split(',')))]

        self.data["Price_numeric"] = self.data["Price"].astype(str).str.replace(r'[\$,]', '', regex=True)
        self.data["Price_numeric"] = pd.to_numeric(self.data["Price_numeric"], errors="coerce")
        
        self.data = self.data[(self.data["Price_numeric"] >= price_range[0]) & (self.data["Price_numeric"] <= price_range[1])]
        
        self.data = self.data.drop('Price_numeric', axis=1)

    def compute_score(self):
        
        self.data["Score"] = (
            self.data["ABV"].astype(str).str.replace('%', '', regex=False).astype(float) * 10
            + self.data["Rating"].astype(float) * self.data["Rate Count"].astype(float)
            - self.data["Price"].astype(str).str.replace(r'[\$,]', '', regex=True).astype(float) * 2
        ).clip(lower=0).round()
        
        self.data = self.data.sort_values("Score", ascending=False)