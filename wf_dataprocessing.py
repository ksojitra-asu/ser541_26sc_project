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
    
    # Feature Engineering & Preprocessing
    
    # 1. Drop unnecessary Customer ID
    if "Customer ID" in df.columns:
        df = df.drop(columns=["Customer ID"])
        
    # 2. Feature Creation
    df["Is_High_Spender"] = (df["Purchase Amount (USD)"] > 75).astype(int)
    
    bins = [0, 25, 50, 150] # <25: Young, 25-50: Adult, >50: Senior
    labels = ["Young", "Adult", "Senior"]
    df["Age_Group"] = pd.cut(df["Age"], bins=bins, labels=labels, right=False)
    
    # 3. Encoding Categorical Data
    # Binary Yes/No Columns mapped to 1/0
    binary_cols = ["Subscription Status", "Discount Applied", "Promo Code Used"]
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({"Yes": 1, "No": 0})
            
    # One-Hot Encoding for remaining nominal categories
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    # Adding string conversions as a failsafe before dummying
    for col in categorical_cols:
        df[col] = df[col].astype(str)
        
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=False, dtype=int)
    
    # 4. Feature Scaling (Standardization)
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    
    # We only scale the continuous features (not the encoded ones)
    scale_cols = ["Age", "Purchase Amount (USD)", "Review Rating", "Previous Purchases"]
    df[scale_cols] = scaler.fit_transform(df[scale_cols])
    
    # saving processed data in data processed folder 
    os.makedirs("data_processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA, index=False)
    
if __name__ == "__main__":
    processing_data()