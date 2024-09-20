# Import Pandas, Numpy and Matplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Exploratory Data Analysis (EDA) of Cash Request 

"""Before diving into cohort analysis, conduct an exploratory data analysis to gain a 
comprehensive understanding of the dataset. Explore key statistics, distributions, 
and visualizations to identify patterns and outliers. EDA will help you make informed 
decisions on data preprocessing and analysis strategies."""

# STEP 1: Read the document and Create a Dataframe
# Document type: CSV
df_cash = pd.read_csv(".\project_dataset\extract - cash request - data analyst.csv")

# STEP 2: Start the Exploratory Analysis

# a: Shape of the DataFrame (rows, columns)
data_shape = df_cash.shape
print("Shape of the DataFrame:")
print(data_shape)

# b: Column Names
column_names = df_cash.columns
print("Column Names:")
print(column_names)

# c: Data types of each column
data_types = df_cash.dtypes
print("Data Types:")
print(data_types)

# d: General Information about the DataFrame
data_info = df_cash.info()
print("General Information about the DataFrame:")
print(data_info)

# e: Statistical Summary
data_summary = df_cash.describe()
print("\nStatistical Summary:")
print(data_summary)

### Data Quality Analysis of Cash Request

"""Assess the quality of the dataset by identifying missing values, 
data inconsistencies, and potential errors. 
Implement data cleaning and preprocessing steps to ensure the reliability of your analysis.
Document any data quality issues encountered and the steps taken to address them."""

# STEP 3: Start the Data Quality Analysis

# a: Check for missing values
# Check for missing values in the DataFrame and clean the dataFrame
missing_values = pd.isnull(df_cash)
df_cash_cleaned = df_cash.drop_duplicates().fillna(0)
# Count missing values in each column
missing_counts = missing_values.sum()

# Count columns with missing values
columns_with_missing = missing_counts[missing_counts > 0].count()

# Check if all columns have missing values
all_columns_missing = missing_counts.all()

# Calculate the total number of missing values
total_missing_values = missing_counts.sum()

# Display the results
print("Missing Values in Each Column:\n", missing_counts)
print("\nNumber of Columns with Missing Values:", columns_with_missing)
print("All Columns Have Missing Values:", all_columns_missing)
print("\nTotal Missing Values in the DataFrame:", total_missing_values)

### Exploratory Data Analysis (EDA) of Fees

"""Before diving into cohort analysis, conduct an exploratory data analysis to gain a 
comprehensive understanding of the dataset. Explore key statistics, distributions, 
and visualizations to identify patterns and outliers. EDA will help you make informed 
decisions on data preprocessing and analysis strategies."""

# STEP 1: Read the document and Create a Dataframe
# Document type: CSV
df_fees = pd.read_csv(".\project_dataset\extract - fees - data analyst - .csv")

# STEP 2: Start the Exploratory Analysis

# a: Shape of the DataFrame (rows, columns)
data_shape = df_fees.shape
print("Shape of the DataFrame:")
print(data_shape)

# b: Column Names
column_names = df_fees.columns
print("Column Names:")
print(column_names)

# c: Data types of each column
data_types = df_fees.dtypes
print("Data Types:")
print(data_types)

# d: General Information about the DataFrame
data_info = df_fees.info()
print("General Information about the DataFrame:")
print(data_info)

# e: Statistical Summary
data_summary = df_fees.describe()
print("\nStatistical Summary:")
print(data_summary)

### Data Quality Analysis of Fees

"""Assess the quality of the dataset by identifying missing values, 
data inconsistencies, and potential errors. 
Implement data cleaning and preprocessing steps to ensure the reliability of your analysis.
Document any data quality issues encountered and the steps taken to address them."""

# STEP 3: Start the Data Quality Analysis

# a: Check for missing values
# Check for missing values in the DataFrame
missing_values = pd.isnull(df_fees)

# Count missing values in each column
missing_counts = missing_values.sum()
df_fees_cleaned = df_fees.drop_duplicates().fillna(0)


# Count columns with missing values
columns_with_missing = missing_counts[missing_counts > 0].count()

# Check if all columns have missing values
all_columns_missing = missing_counts.all()

# Calculate the total number of missing values
total_missing_values = missing_counts.sum()

# Display the results
print("Missing Values in Each Column:\n", missing_counts)
print("\nNumber of Columns with Missing Values:", columns_with_missing)
print("All Columns Have Missing Values:", all_columns_missing)
print("\nTotal Missing Values in the DataFrame:", total_missing_values)


### Exploratory Data Analysis (EDA) of Lexique 

"""Before diving into cohort analysis, conduct an exploratory data analysis to gain a 
comprehensive understanding of the dataset. Explore key statistics, distributions, 
and visualizations to identify patterns and outliers. EDA will help you make informed 
decisions on data preprocessing and analysis strategies."""

# STEP 1: Read the document and Create a Dataframe
# Document type: XLSX
df_lexique = pd.read_excel(".\project_dataset\Lexique - Data Analyst.xlsx")

# STEP 2: Start the Exploratory Analysis

# a: Shape of the DataFrame (rows, columns)
data_shape = df_lexique.shape
print("Shape of the DataFrame:")
print(data_shape)

# b: Column Names
column_names = df_lexique.columns
print("Column Names:")
print(column_names)

# c: Data types of each column
data_types = df_lexique.dtypes
print("Data Types:")
print(data_types)

# d: General Information about the DataFrame
data_info = df_lexique.info()
print("General Information about the DataFrame:")
print(data_info)

# e: Statistical Summary
data_summary = df_lexique.describe()
print("\nStatistical Summary:")
print(data_summary)


### Data Quality Analysis of Lexique

"""Assess the quality of the dataset by identifying missing values, 
data inconsistencies, and potential errors. 
Implement data cleaning and preprocessing steps to ensure the reliability of your analysis.
Document any data quality issues encountered and the steps taken to address them."""

# STEP 3: Start the Data Quality Analysis

# a: Check for missing values
# Check for missing values in the DataFrame
missing_values = pd.isnull(df_lexique)

# Count missing values in each column
missing_counts = missing_values.sum()

# Count columns with missing values
columns_with_missing = missing_counts[missing_counts > 0].count()

# Check if all columns have missing values
all_columns_missing = missing_counts.all()

# Calculate the total number of missing values
total_missing_values = missing_counts.sum()

# Display the results
print("Missing Values in Each Column:\n", missing_counts)
print("\nNumber of Columns with Missing Values:", columns_with_missing)
print("All Columns Have Missing Values:", all_columns_missing)
print("\nTotal Missing Values in the DataFrame:", total_missing_values)


### Metrics to Analyze

"""You will calculate and analyze the following metrics for each cohort:"""

####### METRIC 1. #######
"""**Frequency of Service Usage:** 
Understand how often users 
from each cohort utilize IronHack Payments' cash advance services over time.

For this metric we are going to build the cohorts based on "USER_ID" and "created_at" 
"""

# Number of unique users:
target_columns = ["user_id", "amount"]
columns_to_colapse = ["user_id"]
aggregations = ['count', 'sum', 'mean', 'max', 'min']
users = df_cash_cleaned[target_columns].groupby(by=columns_to_colapse).agg(aggregations)

print("Total number of unique users:")
print(users.count().unique()) # 10798 unique users

# Create the cohorts based on "created_at" and "user_id". Important to group time data by MONTH "M"
df_cash_cleaned['created_at'] = pd.to_datetime(df_cash_cleaned['created_at'])
cohorts = df_cash_cleaned.groupby(df_cash_cleaned['created_at'].dt.to_period("M"))['amount'].count()

# Create the visualization chart using "plt" to see the number of transactions per month, over time
cohorts.plot.bar(figsize=(12, 6))
plt.title('Sergice user over time')
plt.xlabel('Month')
plt.ylabel('Transactions')
plt.show()


####### METRIC 2. #######
"""**Incident Rate:** Determine the incident rate, specifically focusing on payment incidents, for each cohort. 
Identify if there are variations in incident rates among different cohorts."""

# Sort the dataframe by type.
df_fees_sorted = df_fees_cleaned.sort_values(by='type', ascending=True)

# Slice the DataFrame to keep only the rows which column 'type' = 'incident'
df_fees_incidents = df_fees_cleaned[df_fees_cleaned['type'] == "incident"] # DataFrame with all the incidents

# Calculate the number of transactions by count of 'df_fees_incidents'
number_of_incidents = df_fees_incidents['type'].count() # Returns 2196 

# Merge (inner) both "Cash Request" and "Fees" matching the 'cash_request_id' from 'df_fees_incidents with 'id' on 'df_cash'
merged_df = pd.merge(df_fees_incidents, df_cash_cleaned, left_on="cash_request_id", right_on='id', how='inner')

# Group the incidents based on the month the request was created at and count them
merged_df['created_at_y'] = pd.to_datetime(merged_df['created_at_y'])
number_of_incidents_per_month = merged_df.groupby(merged_df['created_at_y'].dt.to_period("M"))['type'].count()


# Calculate the incident rate per month (percentage of number of incidents over total transactions in the same cohort)
incident_rate = (number_of_incidents_per_month / cohorts)*100


# Display the incidents per month on a chart
incident_rate.plot.bar(figsize=(12, 6))
plt.title('Incident Rate Per Month')
plt.xlabel('Month')
plt.ylabel('Percentage(%)')
plt.show()

####### METRIC 3. #######
"""**Revenue Generated by the Cohort:** Calculate the total revenue generated by 
each cohort over months to assess the financial impact of user behavior."""

# Filter the dataFrame 'df_fees' by 'status' = 'accepted'
df_fees_accepted = df_fees_cleaned[df_fees_cleaned['status'] == "accepted"]
merged_df = pd.merge(df_fees_accepted, df_cash_cleaned, left_on="cash_request_id", right_on='id', how='inner')

# Groub 'total_amount' by month based on 'created_at'
merged_df['created_at_y'] = pd.to_datetime(merged_df['created_at_y'])
revenue_per_month = merged_df[['created_at_y', 'total_amount']].groupby(merged_df['created_at_y'].dt.to_period("M"))['total_amount'].count()

# Display the revenue per month on a chart
revenue_per_month.plot.bar(figsize=(12, 6))
plt.title('Revenue Per Month')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.show()

####### METRIC 4. #######
"""**Loss of Revenue due to cancelled transaction**."""


# Filter the dataFrame 'df_fees' by 'status' = 'accepted'

cancelled = df_fees_cleaned[df_fees_cleaned['status']=='cancelled'].reset_index()
merged_cancelled_and_cash = pd.merge(cancelled, df_cash_cleaned, left_on="cash_request_id", right_on='id', how='inner')

# Groub 'total_amount' by month based on 'created_at_y'
merged_cancelled_and_cash['created_at_y'] = pd.to_datetime(merged_cancelled_and_cash['created_at_y'])
loss_revenue = merged_cancelled_and_cash[['created_at_y', 'total_amount']].groupby(merged_cancelled_and_cash['created_at_y'].dt.to_period("M"))['total_amount'].sum()


# Display the loss of revenue per month on a chart
loss_revenue.plot.bar(figsize=(12, 6))
plt.title('Loss Revenue')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.show()

# Convert DataFrames to .csv
cohorts.to_csv('frequency_of_usage.csv', index=True)
revenue_per_month.to_csv('revenue_per_month.csv', index=True)
incident_rate.to_csv('incident_rate.csv', index=True)
loss_revenue.to_csv('loss_revenue.csv',index=True)
print("csv file created")

