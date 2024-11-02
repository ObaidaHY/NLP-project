import pandas as pd

# Load the CSV file
file_path = 'filtered_q1_2021_news.csv'
df = pd.read_csv(file_path)

# Print total number of rows
total_rows = len(df)
print(f"Total number of rows: {total_rows}")

# List of domains to check in the 'publisher' column
domains = ['finance.yahoo.com', 'reuters.com', 'bloomberg.com', 'wsj.com', 'ft.com']

# Iterate over domains and count matches in 'publisher' column
for domain in domains:
    count = df['publisher'].str.contains(domain, na=False).sum()
    print(f"Number of rows with publisher '{domain}': {count}")

