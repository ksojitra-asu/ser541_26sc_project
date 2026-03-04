import os
import itertools
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROCESSED_DATA = os.path.join("data_processed", "processed_shopping_trends.csv")
PATH_OF_SUMMARY = os.path.join("data_processed", "summary.txt")
PATH_OF_CORR = os.path.join("data_processed", "correlations.txt")
DIR_OF_VISUALS = "visuals"

def computing_summary_stats():
    df = pd.read_csv(PROCESSED_DATA)
    
    quantitative_features = [
        "Age",
        "Purchase Amount (USD)",
        "Review Rating",
        "Previous Purchases",
    ]
    
    qualitative_features = ["Category"]
    
    lines = []
    
    lines.append("Summary Statistics - Quantitative Features\n")
    lines.append("Feature\tMin\tMax\tMedian\n")
    for col in quantitative_features:
        col_series = df[col].dropna()
        min_val = col_series.min()
        max_val = col_series.max()
        median_val = col_series.median()
        lines.append(f"{col}\t{min_val:.3f}\t{max_val:.3f}\t{median_val:.3f}\n")
    
    lines.append("\nSummary Statistics - Qualitative Features\n")
    lines.append("Features\tNum Categories\tMost Frequent\tLeast Frequent\n")
    for col in qualitative_features:
        value_counts = df[col].value_counts()
        num_categories = value_counts.shape[0]
        max_count = value_counts.max()
        min_count = value_counts.min()
        most_freq = ", ".join(value_counts[value_counts == max_count].index.tolist())
        least_freq = ",".join(value_counts[value_counts == min_count].index.tolist())
        lines.append(f"{col}\t{num_categories}\t{most_freq}\t{least_freq}\n")
        
    os.makedirs("data_processed", exist_ok = True)
    with open(PATH_OF_SUMMARY, "w", encoding="utf-8") as f:
        f.writelines(lines)
        
def computing_correlations():
    df = pd.read_csv(PROCESSED_DATA)

    quantitative_features = [
        "Age",
        "Purchase Amount (USD)",
        "Review Rating",
        "Previous Purchases",
    ]

    correlations = df[quantitative_features].corr(method="pearson")

    os.makedirs("data_processed", exist_ok=True)
    with open(PATH_OF_CORR, "w", encoding="utf-8") as f:
        f.write("Correlation Matrix\n")
        f.write(correlations.to_string()) 
        f.write("\n")
        
if __name__ == "__main__":
    computing_summary_stats()
    computing_correlations()