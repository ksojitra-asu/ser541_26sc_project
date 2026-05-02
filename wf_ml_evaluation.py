import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")
EVAL_DIR = os.path.join(BASE_DIR, "evaluation")
SUMMARY_FILE = os.path.join(EVAL_DIR, "summary.txt")

def evaluate_models():
    # 1. Loading purely testing vault
    X_test = pd.read_csv(os.path.join(BASE_DIR, "data_processed", "X_test.csv"))
    y_test = pd.read_csv(os.path.join(BASE_DIR, "data_processed", "y_test.csv")).values.ravel()
    
    out_lines = []
    out_lines.append("--- ML Evaluation Matrix: Subscription Status ---\n")
    out_lines.append(f"{'Model Type':<30} | {'Accuracy':<10} | {'F1-Score':<10}\n")
    out_lines.append("-" * 60 + "\n")
    
    def log_metric(name, y_pred):
        acc = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        out_lines.append(f"{name:<30} | {acc:.4f}     | {f1:.4f}\n")
    
    # 2. Evaluate Baseline Model
    baseline = joblib.load(os.path.join(MODELS_DIR, "baseline_model.pkl"))
    # Base model evaluates exclusively on Age & Purchases
    y_pred_base = baseline.predict(X_test[["Age", "Previous Purchases"]])
    log_metric("Baseline (Logistic)", y_pred_base)
    
    # 3. Evaluate Actual Model
    actual = joblib.load(os.path.join(MODELS_DIR, "actual_model.pkl"))
    y_pred_act = actual.predict(X_test)
    log_metric("Actual (RandomForest)", y_pred_act)
    
    # --- Generating Tune Alternative Models ---
    # We rebuild the identically-sharded training state to ensure scientific validation parity
    df = pd.read_csv(os.path.join(BASE_DIR, "data_processed", "processed_shopping_trends.csv"))
    X = df.drop(columns=["Subscription Status"])
    y = df["Subscription Status"]
    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train & Evaluate Alternates
    # Alt 1: Pruned Random Forest (max_depth=5 restricts tree depth specifically to avoid memorizing/overfitting)
    alt_1 = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
    alt_1.fit(X_train, y_train)
    log_metric("Alt 1: RF (Max Depth=5)", alt_1.predict(X_test))
    
    # Alt 2: Lightweight Random Forest (n_estimators=10 reduces logic tree volume to test speed/accuracy drops)
    alt_2 = RandomForestClassifier(n_estimators=10, random_state=42)
    alt_2.fit(X_train, y_train)
    log_metric("Alt 2: RF (Estimators=10)", alt_2.predict(X_test))
    
    # Alt 3: Decision Tree Classifier (Alternative base algorithm testing singular logic boundaries instead of forests)
    alt_3 = DecisionTreeClassifier(random_state=42)
    alt_3.fit(X_train, y_train)
    log_metric("Alt 3: Decision Tree", alt_3.predict(X_test))
    
    # 5. Output File Creation
    os.makedirs(EVAL_DIR, exist_ok=True)
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.writelines(out_lines)
    
    for row in out_lines:
        print(row, end="")
    print(f"\nStats successfully exported to {SUMMARY_FILE}!")

if __name__ == "__main__":
    evaluate_models()
