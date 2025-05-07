🧼 Data Cleaning Summary – Missing Data Handling in Pandas
This notebook demonstrates various techniques to identify, visualize, and handle missing data using Python libraries like Pandas, NumPy, and Seaborn. These techniques are crucial in preparing clean datasets for data analysis or machine learning.

📊 Dataset Overview
A sample dataset was created with three columns:

Temperature

Humidity

Situation

Some entries were intentionally left missing (NaN) to simulate real-world scenarios.

🔎 Step-by-Step Summary
✅ 1. Identifying Missing Values
df.isna() highlights missing values.

df.isna().sum() gives the count of missing values in each column.

📌 2. Visualizing Missing Data
A heatmap was created using seaborn.heatmap() to visually spot missing entries.

🧹 3. Handling Missing Values
Drop rows with missing values:

df.dropna() removes all rows containing any NaN.

df.dropna(how="all") removes rows where all values are NaN.

Fill missing values:

df.fillna(method='ffill'): Forward fill – fills NaN with the value above.

df.fillna(method='bfill'): Backward fill – fills NaN with the value below.

df['Temperature'].fillna(mean_value, inplace=True): Fills missing values with the mean of the column.

♻️ 4. Removing Duplicates
df.drop_duplicates() was used to retain only the first occurrence of duplicate rows.

✅ Final Output
After cleaning:

All missing data was handled using appropriate methods.

The dataset was free from duplicates and ready for analysis.