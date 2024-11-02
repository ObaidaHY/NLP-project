import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")   
SUMMARY_COLUMN = "summary" 

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

 

try:
    # Connect to the database
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    print("Connection successful!")

    # Create a cursor object
    cursor = connection.cursor()

    # Query to fetch summaries from the table
    #query = f"SELECT count(*) FROM {TABLE_NAME};" 
    query = f"SELECT DISTINCT published_date FROM {TABLE_NAME};"

    # Execute the query
    cursor.execute(query)

    # Fetch the results
    rows = cursor.fetchall()

    # Validate if any summaries were fetched
    if rows:
        print("Summaries fetched successfully:")
        for idx, row in enumerate(rows):
            print(f"{idx + 1}: {row[0]}")
    else:
        print("No summaries found or the column is empty.")
        
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
