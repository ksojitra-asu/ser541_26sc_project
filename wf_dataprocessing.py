import os
import pandas as pd

ORIGINAL_DATA = os.path.join("data_original", "shopping_trends.csv")
PROCESSED_DATA = os.path.join("data_processed", "processed_shopping_trends.csv")

def processing_data():
    # loading original data
    df = pd.read_csv(ORIGINAL_DATA)
    
    # ensuring data types are correct in numeric columns
    numeric_columns = [
        "Age",
        "Purchase Amount (USD)",
        "Review Rating",
        "Previous Purchases",
    ]
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors = "coerce")
    
    # dropping empty rows in numeric_columns 
    df = df.dropna(subset = numeric_columns, how = "all")
    
    # handling outliers in Purchase Amount field
    purchase = df["Purchase Amount (USD)"]
    lower = purchase.quantile(0.01)
    upper = purchase.quantile(0.99)

    df["Purchase Amount (USD)"] = purchase.clip(lower, upper)
    
    # saving processed data in data processed folder 
    os.makedirs("data_processed", exist_ok = True)
    df.to_csv(PROCESSED_DATA, index = False)
    
if __name__ == "__main__":
    processing_data()