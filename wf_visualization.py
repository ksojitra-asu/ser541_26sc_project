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
        
# if __name__ == "__main__":
#     computing_summary_stats()
#     computing_correlations()


def generating_plots():
    df = pd.read_csv(PROCESSED_DATA)
    os.makedirs(DIR_OF_VISUALS, exist_ok=True)

    # Shared settings: style and palette for all plots
    sns.set_theme(style="whitegrid", font_scale=1.1)
    PALETTE_SCATTER = "husl"  

    quantitative_features = [
        "Age",
        "Purchase Amount (USD)",
        "Review Rating",
        "Previous Purchases",
    ]
    qualitative_features = ["Category"]

    for x_col, y_col in itertools.combinations(quantitative_features, 2):
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(
            data=df,
            x=x_col,
            y=y_col,
            hue="Category",
            palette=PALETTE_SCATTER,
            alpha=0.7,
            s=40,
            edgecolor="white",
            linewidth=0.3,
            ax=ax,
        )
        
        sns.regplot(
            data=df,
            x=x_col,
            y=y_col,
            scatter=False,
            color="black",
            line_kws={"linestyle": "--", "linewidth": 2},
            ax=ax,
        )
        corr = df[x_col].corr(df[y_col])
        ax.set_title(f"{x_col} vs {y_col} (r = {corr:.3f})")
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
        plt.tight_layout()
        filename = f"scatter_{x_col.replace(' ', '_')}_vs_{y_col.replace(' ', '_')}.png"
        plt.savefig(os.path.join(DIR_OF_VISUALS, filename), dpi=FIG_DPI, bbox_inches="tight")
        plt.close()

    
    for col in qualitative_features:
        value_counts = df[col].value_counts()
        value_counts = value_counts.sort_values(ascending=True)  
        n_cats = len(value_counts)
        colors = sns.color_palette(PALETTE_SCATTER, n_colors=n_cats)
        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.barh(value_counts.index, value_counts.values, color=colors, edgecolor="white", linewidth=0.5)
        ax.set_xlabel("Count")
        ax.set_ylabel(col)
        ax.set_title(f"Distribution of {col} (n = {len(df):,})")
        for bar, val in zip(bars, value_counts.values):
            ax.text(val + 20, bar.get_y() + bar.get_height() / 2, f"{val:,}", va="center", fontsize=9)
        plt.tight_layout()
        filename = f"hist_{col.replace(' ', '_')}.png"
        plt.savefig(os.path.join(DIR_OF_VISUALS, filename), dpi=FIG_DPI, bbox_inches="tight")
        plt.close()


if __name__ == "__main__":
    computing_summary_stats()
    computing_correlations()
    generating_plots()