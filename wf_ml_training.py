import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DATA = os.path.join(BASE_DIR, "data_processed", "processed_shopping_trends.csv")
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, "data_processed")

def training_models():
    # 1. Data Loading
    df = pd.read_csv(PROCESSED_DATA)
    
    # 2. Target Isolation
    # PIVOT: We are now predicting binary Subscription Status.
    target_col = "Subscription Status"
    
    # Feature Matrix X and Target Vector y
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Split the dataset into 80% training data and 20% validation testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Baseline Model Generation (Classification)
    # Constraint: Must use less data / lower complexity. 
    # We will use simple Logistic Regression on purely numeric age & loyalty features
    baseline_features = ["Age", "Previous Purchases"]
    
    baseline_model = LogisticRegression(random_state=42)
    baseline_model.fit(X_train[baseline_features], y_train)
    
    # 4. Actual Predictive Model Generation
    # We will use a RandomForestClassifier over the entire robust feature matrix
    actual_model = RandomForestClassifier(n_estimators=100, random_state=42)
    actual_model.fit(X_train, y_train)
    
    # 5. Save Models & Test Splits
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    joblib.dump(baseline_model, os.path.join(MODELS_DIR, "baseline_model.pkl"))
    joblib.dump(actual_model, os.path.join(MODELS_DIR, "actual_model.pkl"))
    
    # Exporting test sets to data_processed/ ensures our future evaluation scripts
    # test against the exact same hold-out data.
    os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
    X_test.to_csv(os.path.join(DATA_PROCESSED_DIR, "X_test.csv"), index=False)
    y_test.to_csv(os.path.join(DATA_PROCESSED_DIR, "y_test.csv"), index=False)
    
    print("Baseline (Logistic) and Actual (Random Forest) classification models saved securely to /models.")

if __name__ == "__main__":
    training_models()
