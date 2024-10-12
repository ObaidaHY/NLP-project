from yahooquery import search
import yfinance as yf
import json
import pandas as pd
import numpy as np


def get_financial_data(tickers):
    # List of company tickers
    # tickers = {
    #     # Note: You will only get historical data for Twitter before the acquisition.
    #     'Twitter': 'TWTR'
    # }

    # Define start and end dates for the time period you want
    start_date = '2010-01-01'
    end_date = '2024-04-15'

    # Iterate through each company and download historical stock data
    for company, ticker in tickers.items():
        try:
            print(f"Downloading data for {company} ({ticker})...")

            # Get historical stock data for the company
            stock_data = yf.Ticker(ticker)
            history = stock_data.history(
                start=start_date, end=end_date, interval='1mo')  # Monthly data

            # Save the historical data to a CSV file
            file_name = f"./financialData/{company.lower()}_stock_data.csv"
            history.to_csv(file_name)

            print(f"Data for {company} saved to {file_name}")

        except Exception as e:
            print(
                f"Couldn't get data for company : {company}. Please check if ticker is correct")
            continue

        print("Download complete.")

# Import yahooquery for searching ticker symbols


def get_ticker(company_name):
    try:
        # Perform search for the company
        results = search(company_name)

        # Check if results are valid and contain quotes
        if results and 'quotes' in results:
            # Find the best match for the company
            ticker = results['quotes'][0]['symbol']
            return ticker
        else:
            print(f"No ticker found for {company_name}.")
            return None
    except Exception as e:
        print(f"An error occurred while searching for {company_name}: {e}")
        return None


# Example usage
# company_name = "Twitter"
# ticker = get_ticker(company_name)
# if ticker:
#     print(f"The ticker for {company_name} is {ticker}.")
# else:
#     print(f"No ticker found for {company_name}.")


# Function to get tickers for a list of company names and save to JSON
def save_company_tickers_to_json(company_names, json_file):
    company_ticker_map = {}

    # Loop through each company name
    for company in company_names:
        ticker = get_ticker(company)
        if ticker:
            company_ticker_map[company] = ticker
            print(f"Found ticker for {company}: {ticker}")
        else:
            print(f"No ticker found for {company}")

    # Save the dictionary to a JSON file
    with open(json_file, 'w') as f:
        json.dump(company_ticker_map, f, indent=4)

    print(f"Company-ticker map saved to {json_file}")


# Example usage
# company_names = ["Twitter", "Microsoft", "Apple", "Amazon"]
# json_file = "company_tickers.json"
# save_company_tickers_to_json(company_names, json_file)


# Load data and extract unique company names
def extract_unique_companies(csv_file):
    df = pd.read_csv(csv_file)
    unique_companies = df['company'].unique().tolist()
    return unique_companies


def load_tickers_and_get_data(json_file):
    try:
        # Load company-ticker mapping from JSON file
        with open(json_file, 'r') as f:
            tickers = json.load(f)

        # Send the tickers to the get_financial_data function
        get_financial_data(tickers)

    except FileNotFoundError:
        print(f"File {json_file} not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file {json_file}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
csv_file_path = 'layoffs.csv'  # Replace with the path to your CSV file
unique_companies = extract_unique_companies(csv_file_path)
json_file = "company_tickers.json"
save_company_tickers_to_json(unique_companies, json_file)
load_tickers_and_get_data(json_file)
