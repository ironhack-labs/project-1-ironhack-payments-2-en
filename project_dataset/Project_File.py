import pandas as pd

# Use the raw URL of the CSV file
url = "https://raw.githubusercontent.com/Selinsight/project-1-ironhack-payments-2-en/main/project_dataset/extract%20-%20cash%20request%20-%20data%20analyst.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataframe to verify
print(df.head())