#### SER541: Project Proposal
#### Title: Recognizing Differences in Purchase Behavior among E-Commerce Demographics
#### Karnika Sojitra
#### Date: 03/23/2026

**Keywords:**
E-commerce analytics, Purchasing behavior analysis, Consumer segmentation

**Description:** 
In order to identify connections between demographics, buying habits, and transaction features, this project examines the purchasing behavior of online shoppers. 3,900 customers' demographics, purchase preferences, and transactional information are included in the dataset.
There are some research questions: Which demographic variables indicate how much a purchase will cost? What unique consumer groups are there according to their purchasing habits? What differences exist between groups in the use of discounts? How do customer value and shopping frequency relate to each other?
It focuses on knowledge discovery-finding behavioral insights.

**Research Objectives:**
* **RO1:** To describe the demographic and transactional trends within the Shopping Trends dataset.
* **RO2:** To predict the value of the Purchase Amount (USD) for a customer based on their demographics and shopping interactions.
* **RO3:** To identify distinct customer segments based on their purchasing behavior and demographics.
* **RO4:** To compare the effectiveness of different machine learning algorithms in predicting purchase behavior.
* **RO5:** To provide actionable insights to e-commerce businesses for improving customer engagement and sales.

**Preregistration:**
* **Expected Input Features:** Age, Previous Purchases, Review Rating, Season and Category.
* **Target Feature:** Purchase Amount (USD).
* **Significant Input Features:** Age (A), Previous Purchases (B), Review Rating, Season (C).
* **Individual Hypotheses:**
  * **Age (A):** We hypothesize that older customers will generally have a higher Purchase Amount. *Justification:* Older individuals tend to have more disposable income and brand loyalty compared to younger demographics, leading to higher-value purchases.
  * **Previous Purchases (B):** We hypothesize that customers with more previous purchases will spend more per transaction. *Justification:* Returning customers demonstrate trust in the platform and are subsequently more willing to make bulk or expensive orders.
  * **Season (C):** We hypothesize that purchases made in Winter and Fall will be higher in value than Spring and Summer. *Justification:* Winter apparel and outerwear are physically larger and generally more expensive to manufacture than light summer apparel.

* **Pairwise Hypotheses:**
  * **A-B (Age & Previous Purchases):** We hypothesize that as Age and Previous Purchases increase together, the prediction will be significantly higher. *Justification:* Older, loyal customers represent a compounded group of high disposable income and high trust, acting as the most reliable source of high revenue.
  * **B-C (Previous Purchases & Season):** We hypothesize high Previous Purchases combined with the Winter season will yield the highest purchase amounts. *Justification:* Loyal customers doing their major holiday or winter shopping will spend the most per transaction.
  * **A-C (Age & Season):** We hypothesize that Age will be less predictive of spending in Summer than in Winter. *Justification:* Winter coats are a necessary, expensive item across all age groups, whereas summer spending is more discretionary and age-dependent.

**Intellectual Merit:**
This project advances scientific knowledge by mapping previously unexplored interactions between demographic variables and seasonal transaction patterns in recent e-commerce environments. While basic consumer segmentation is a known domain, this research produces new knowledge by comparing the predictive efficacy of distinct machine learning algorithms to determine which modeling techniques are uniquely optimal for capturing the volatility of modern consumer behavior. Furthermore, by isolating non-linear interactions between trust metrics (like previous purchases) and demographics, the study seeks to discover entirely novel, nuanced customer segments that challenge traditional marketing boundaries. Ultimately, this will yield statistically validated, original insights into the causal drivers of high-value online transactions. 

**Data Sourcing:** 
Mendeley Data (DOI:10.17632/xv99b2mtfk.1), published in January 2025 by Hariharan S. and licensed under CC by 4.0, is the source of dataset, which includes 3,900 customer records with transactional details, buying preferences, and demographics. Retrieval: After agreeing to the license terms, a CSV or Excel file can be downloaded directly from the Mendeley Data platform. The majority of variables in the data structure are quantitative; during munging, categorical variables like gender, location, and product categories need to be encoded. Preprocessing requirements will be ascertained, missing values or outliers will be found, and completeness will be evaluated. 

**Background Knowledge:**
1. https://www.pewresearch.org/internet/2016/12/19/online-shopping-and-e-commerce/
2. https://www.digitalcommerce360.com/2024/09/13/free-and-fast-shipping-consumers-delivery-2024/
3. https://link.springer.com/article/10.1007/s12061-021-09397-0

**Related Work:**
1. https://doi.org/10.69882/adba.iteb.2024071
2. https://doi.org/10.54254/2755-2721/55/20241475
3. https://doi.org/10.2174/0123520965380645250505070035
4. https://doi.org/10.54938/ijemdcsai.2022.01.1.84
5. https://doi.org/10.1371/journal.pone.0243105
6. https://doi.org/10.54691/bcpbm.v49i.5411
