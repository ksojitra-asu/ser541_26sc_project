**SER594: Exploratory Data Munging and Visualization**

**Title:** Shopping Trends Analysis based on Customer Demographics and Purchase Behavior

**Author:** Anonymous

**Date:** 03/04/2026

**Basic Questions:** 
Author: Hariharan S.
Construction Date: 15/01/2025
Number of records: 3900 records with 19 attributes

**Field Description:**
Customer ID: Unique Identifier which differentiates each customer
Age: Age of customer
Gender: Gender of customer
Item Purchased: Items which customer bought
Category: Category of the purchased product
Purchased Amount (USD): Price in USD of the purchased products
Location: Customer's location
Size: Size of the item purchased
Color: Color of the item purchased
Season: Season during customer made the purchase
Review Rating: Rating provided by customer
Subscription Status: Whether customer has subscribed or not
Payment Method: Method of payment used for purchase
Shipping Type: Type of shipping selected
Discount Applied: If Discount is applied or not
Promo Code Used: Whether if a promo code was applied or not
Previous Purchases: No. of previous purchases made by customer
Preferred Payment Method: Method of payment preferred by customer
Frequency of Purchases: Frequency of purchases made by customer

**MD5 hash:** 2c08b5fc431fa75d81cb90aa2092e398

**Interpretable Records:**
Data based on Row 11:
-Customer ID: 10
-Age: 57
-Gender: Male
-Item Purchased: Handbag
-Category: Accessories
-Purchased Amount (USD): 31
-Location: Missouri
-Size: M
-Color: Pink
-Season: Spring
-Review Rating: 4.8
-Subscription Status: Yes
-Payment Method: PayPal 
-Shipping Type: 2-Day Shipping
-Discount Applied: Yes
-Promo Code: Yes
-Previous Purchases: 4
-Preferred Payment Method: Cash
-Frequency of Purchases: Quarterly

**English Explanation:**
The record described here is of a 57 year old male customer from Missouri who purchased a handbag of pink color in Spring. He choose 2-day shipping and used PayPal to pay 31USD for the bag. He also applied discount as well as promo code and previously made 4 purchases. Overall, he prefers cash and he has subscribed to the service. 

**Reasonableness:**
For a real world purchasing scenario, the combination of location, age, item type and purchase amount makes sense. The frequency of transactions and the number of prior purchases are consistent with a reasonably devoted client, and the purchase amount is within a reasonable range of apparel.

Data based on Row 107:
-Customer ID: 106
-Age: 69
-Gender: Make
-Item Purchased: Backpack
-Category: Accessories
-Purchased Amount (USD): 96
-Location: New York
-Size: M
-Color: Charcoal
-Season: Fall
-Review Rating: 3.6
-Subscription Status: Yes
-Payment Method: Bank Transfer
-Shipping Type: Next Day Air
-Discount Applied: Yes
-Promo Code: Yes
-Previous Purchases: 4
-Preferred Payment Method: Bank Transfer
-Frequency of Purchases: Anually

**English explanation:**
This record details a 69 year old male consumer from New York who purchased a charcoal colored backpack during Fall. He made 4 prior transactios, applied discount as well as promo code and paid 96USD using bank transfer. He shops about every 2 weeks, subscribes to the service, and generally prefers to do bank transfers.

**Reasonableness:**
In real-world the integration of item type, location, purchase amount and age makes sense. For a backpack as an accessory, the purchase price is a little higher than usual. The frequency of purchases combined with previous transactions indicates that he does not shop frequently.

**Background Domain Knowledge:**
In order to make predictions about inventory, pricing, and marketing, retail and e-commerce companies primarily rely on their knowledge of consumer buying habits. Specifically, a comprehensive picture of how individuals actually shop in everyday situations is provided by customer-level data that integrates demographics, purchase amounts, product categories, and repeat behavior. This study focuses on retail buying trends and uses transactional data to investigate the relationship between spending and satisfaction and variables including age, product type, season, and previous purchases.

There is a high correlation between variations in shopping behavior and demographic characteristics such as age, gender, and geography. For instance, younger consumers are frequently characterized as being more receptive to rapidly evolving fashion trends and internet advertising, whereas elderly consumers can place a higher value on dependability and quality than novelty [Source 1]. Customers in warmer places may choose lighter clothing and seasonal accessories, while those in colder regions typically purchase more coats and warm clothing [Source 2]. Geographical considerations, such as temperature and regional culture, may have an impact on the kind of things that are purchased. This dataset, which contains fields like 'Age', 'Gender', and 'Location' across several U.S. states, directly relates to these patterns.

Lastly, shipping and payment choices play a significant role in contemporary consumer behavior. Due to consumer preferences for convenience and trust, digital wallets and online payment platforms have grown beyond the use of traditional cash and credit cards [Source 3]. Similar trade-offs between cost and speed are reflected in shipping options like free standard delivery versus expensive expedited shipment, which depend on how urgently buyers need their things. Features like 'Payment Method', 'Preferred Payment Method', and 'Shipping Type' in this dataset provide a condensed picture of these preferences. When combined, these characteristics assist contextualize the patterns found in the exploratory study and offer a domain-relevant context for examining shopping trends.

**Sources:**
1. [https://www.pewresearch.org/internet/2016/12/19/online-shopping-and-e-commerce/]
2. [https://link.springer.com/article/10.1007/s12061-021-09397-0#Sec7]
3. [https://www.digitalcommerce360.com/2024/09/13/free-and-fast-shipping-consumers-delivery-2024/]

**Dataset Generality:**
The dataset suggests regional and demographic diversity as it spans several US states and a range of ages (for example, from teens to older persons). It helps reflect variation in seasonal demand by including many seasons (Spring, Summer, Fall, and Winter) and multiple product categories (clothing, footwear, accessories, and outerwear). Analysis across various loyalty levels is made possible by purchase behavior variables (Purchase Amount (USD), Previous Purchases, Frequency of Purchases, Subscription Status), which display both occasional and frequent buyers.

It is still a limited sample, though, and it could be skewed by:
The specific store/retailer it represents.
Limited time period of data collection.

Overall, the diversity of demographics, product categories, and seasons indicates that the dataset is a fairly representative sample of average retail purchasing behavior within its target market, even though it is not a perfect representation of all worldwide customers.

**Data Transformations:**
1. Type conversion (numeric columns)
The columns Age, Purchase Amount (USD), Review Rating, and Previous Purchases were converted to numeric types using pd.to_numeric(..., errors="coerce"). Any non-numeric values in these columns become missing (NaN). This step does not change the meaning of the data: valid numbers are unchanged, and only invalid entries are marked as missing so that later statistics and correlations are computed on valid numeric values only.

2. Dropping rows with missing key numeric data
Rows where all four of the numeric columns (Age, Purchase Amount (USD), Review Rating, Previous Purchases) were missing were dropped with dropna. Only rows with no usable numeric information for these core fields are removed. Rows with at least one valid value in these columns are kept. This avoids discarding usable data while ensuring that summary statistics and correlations are not distorted by rows with no numeric content.

3. Outlier handling for Purchase Amount (USD)
Extreme values in Purchase Amount (USD) were capped using the 1st and 99th percentiles: values below the 1st percentile were set to the 1st percentile, and values above the 99th percentile were set to the 99th percentile. No new outliers are introduced; existing extremes are only bounded.

4. Unchanged fields
All other columns (e.g., Customer ID, Gender, Item Purchased, Category, etc.) were left unchanged. No labels or categories were altered, so the semantics of the data are preserved.

**Visualizations:**

1. Histogram: Distribution of Category
The histogram shows that Clothing is the most frequent purchase category, followed by Accessories, Footwear, and Outerwear. This indicates that in the dataset, apparel (clothing and related items) dominates transaction volume, while Outerwear is the least common. The imbalance across categories is relevant for understanding where most of the observed shopping behavior occurs.

2. Scatter plot: Age vs Purchase Amount (USD) 
The scatter plot shows customers spread across the full range of ages (18–70) and purchase amounts, with no strong linear relationship (correlation r is close to zero). Points colored by category indicate that no single product category is confined to a specific age or spending band; all categories appear across the plot. The flat trend line supports that, in this sample, age alone does not predict purchase amount in a linear way.

3. Scatter plot: Age vs Previous Purchases
Older and younger customers both show a wide range of previous purchase counts, and the correlation is weak (r ≈ 0.04). So customer tenure (previous purchases) does not increase or decrease strongly with age in this dataset. The mix of categories across the plot suggests that repeat-purchase behavior is not limited to a particular age group or product type.

4. Scatter plot: Age vs Review Rating 
The plot shows that customers of all ages give a similar spread of review ratings; the correlation between age and rating is very weak (r ≈ −0.02). No clear pattern suggests that older or younger customers rate purchases higher or lower. The trend line is nearly flat, indicating that in this sample, age does not linearly predict satisfaction as measured by review rating.

5. Scatter plot: Purchase Amount (USD) vs Review Rating  
There is no strong linear association between how much a customer spent and the review rating they gave (r ≈ 0.03). Higher and lower purchase amounts appear at all rating levels, indicating that satisfaction (as reflected in ratings) is not simply tied to spending in this sample. The trend line is nearly flat, which is consistent with the weak correlation.

6. Scatter plot: Purchase Amount (USD) vs Previous Purchases  
The plot shows that repeat customers (high previous purchases) and first-time or low-frequency customers (low previous purchases) both make purchases across a similar range of amounts; the correlation is close to zero. So in this data, purchase amount per transaction does not increase or decrease in a linear way with how many previous purchases a customer has made, suggesting that basket size is relatively independent of purchase history.

7. Scatter plot: Review Rating vs Previous Purchases  
Review ratings and previous purchase counts show no strong linear relationship (r ≈ 0.004). Customers with few prior purchases and those with many prior purchases both give a similar range of ratings, so satisfaction does not appear to increase or decrease with customer tenure in this dataset. The nearly flat trend line supports that review rating and repeat-purchase behavior are largely independent in this sample.