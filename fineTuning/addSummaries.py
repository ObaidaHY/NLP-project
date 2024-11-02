import pymysql
import pandas as pd
from datetime import datetime, timedelta

# Database connection details
DB_HOST = "mysqlsrv1.cs.tau.ac.il"
DB_USER = "markfesenko"
DB_PASSWORD = "3mZhryk&^5yP"
DB_NAME = "markfesenko"

# Connect to the database
def connect_to_db():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection



# Fetch summaries for a specific time window before a layoff date
def fetch_summaries_within_window(layoff_timestamp, days_before, connection, table_name="summaries"):
    layoff_date = datetime.fromtimestamp(layoff_timestamp)
    start_date = layoff_date - timedelta(days=days_before)
    

    query = f"""
    SELECT summary 
    FROM {table_name}
    WHERE published_date BETWEEN %s AND %s;
    """
    
    with connection.cursor() as cursor:
        cursor.execute(query, (start_date, layoff_date))
        results = cursor.fetchall()
    
    # Concatenate summaries into a single text sample
    summaries_text = " ".join([row['summary'] for row in results])
    print(layoff_date)
    print(start_date)
    print(summaries_text)
    print(len(summaries_text))
    return summaries_text

# Extend layoff_data to include news summaries for 7, 14, and 30 days before each layoff date
def add_news_summaries(layoff_data, connection):
    # Initialize empty lists to store the news summaries for each window
    news_7_days = []
    news_14_days = []
    news_30_days = []

    # Iterate through each row in layoff_data
    for index, row in layoff_data.iterrows():
        layoff_timestamp = row['Date_layoffs']
        
        # Fetch news summaries for each time window
        news_7 = fetch_summaries_within_window(layoff_timestamp, 7, connection)
        return
        news_14 = fetch_summaries_within_window(layoff_timestamp, 14, connection)
        news_30 = fetch_summaries_within_window(layoff_timestamp, 30, connection)
        
        # Append the summaries to the respective lists
        news_7_days.append(news_7)
        news_14_days.append(news_14)
        news_30_days.append(news_30)

    # Add the new text columns to layoff_data
    layoff_data['news_7_days'] = news_7_days
    layoff_data['news_14_days'] = news_14_days
    layoff_data['news_30_days'] = news_30_days

    return layoff_data

# Connect to the database
connection = connect_to_db()

# Example layoff_data with Date_layoffs as Unix timestamps
layoff_data = pd.read_csv("finalDataset.csv")

# Add news summaries for each layoff date
layoff_data_with_news = add_news_summaries(layoff_data, connection)

# Save the updated dataset to a CSV
layoff_data_with_news.to_csv("layoff_data_with_news.csv", index=False, encoding='utf-8')

print("Data saved to layoff_data_with_news.csv")

# Close the database connection
connection.close()
