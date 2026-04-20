import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

def predict_single_input():
    # 1. Load the Actual Model
    model_path = os.path.join(MODELS_DIR, "actual_model.pkl")
    actual_model = joblib.load(model_path)
    
    # 2. Extract an isolated input
    X_test_path = os.path.join(MODELS_DIR, "X_test.csv")
    X_test = pd.read_csv(X_test_path)
    
    # Extract the very first row to simulate a fresh incoming user request
    single_input = X_test.iloc[[0]] 
    
    # 3. Predict the Output 
    # (Predict if this user will have Subscription Status = 1)
    prediction = actual_model.predict(single_input)
    
    print("\n--- Isolated Prediction Results ---")
    print("Simulated Incoming Target User Features:")
    
    # Print the features that have data > 0 to save space on console text
    active_features = [col for col in single_input.columns if single_input.iloc[0][col] != 0]
    print(single_input[active_features].to_string())
    
    print("\nModel Output for Subscription Status (1=Yes, 0=No):", prediction[0])
    
if __name__ == "__main__":
    predict_single_input()
