# Project Formulation: ML Evaluation

### 1. Title
Recognizing Differences in Purchase Behavior among E-Commerce Demographics

### 2. Author
Karnika Sojitra

### 3. Date
04/20/2026

### 4. Evaluation Metrics
For this classification modeling pipeline, the two distinct metrics used are:
- **Accuracy**: Indicates the overall correctness of the model logic (Total Correct Predictions / Total Predictions). This was appropriate to evaluate exactly how frequently the model predicts the correct binary membership over the test suite. 
- **F1-Score**: Calculates the harmonic mean of Precision and Recall. This metric is mathematically crucial because retail data is famously unbalanced (most users don't buy or subscribe). If a model simply guessed "No" 100% of the time, the dataset accuracy might intuitively read "very high" despite possessing zero predictive power. F1-Score accurately penalizes blind negative-guessing and rewards models that physically learn the traits of actual subscribers.

### 5. Alternative Models
- **Baseline Model**: Constructed utilizing an intentionally naive `LogisticRegression` class mapping purely two basic variables (`Age` and `Previous Purchases`). During evaluation, it completely flat-lined (F1-score: `0.0000`, Accuracy: `0.7154` simply because it purely guessed 'no' natively).
- **Alternative 1: Restricted Random Forest (Max Depth = 5)**: Constructed aggressively by capping tree depth to 5 branches to test if reducing data fragmentation reduced testing noise. Evaluation proved it underperformed our unconstrained model severely, dropping F1 logic to `0.6351`.
- **Alternative 2: Lightweight Random Forest (Estimators = 10)**: Constructed by artificially limiting the ensemble count from 100 deep-trees to 10 low-impact trees, measuring for speed vs accuracy cost. Evaluation fared poorly: F1-score immediately crashed to `0.6347`.
- **Alternative 3: Simple Decision Tree**: Constructed using a single logical `DecisionTreeClassifier()` without any algorithmic voting ensemble. It logically outperformed the constrained Forests (F1: `0.6652`, Accuracy: `0.8026`) but continued to fall heavily behind our original model. 

### 6. Best Model
The **Actual Predictive Model (Random Forest Classifier)** was indisputably the highest-performing matrix across the board. By unleashing 100 separate estimators securely across our finalized dataset, it safely navigated all engineered/encoded patterns—hitting an **Accuracy of 82.82%** alongside an **F1-Score of 0.7500**.