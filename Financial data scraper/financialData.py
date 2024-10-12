import yfinance as yf

# List of company tickers
tickers = {
    'Twitter': 'TWTR'  # Note: You will only get historical data for Twitter before the acquisition.
}

# Define start and end dates for the time period you want
start_date = '2010-01-01'
end_date = '2024-04-15'

# Iterate through each company and download historical stock data
for company, ticker in tickers.items():
    print(f"Downloading data for {company} ({ticker})...")

    # Get historical stock data for the company
    stock_data = yf.Ticker(ticker)
    history = stock_data.history(start=start_date, end=end_date, interval='1mo')  # Monthly data

    # Save the historical data to a CSV file
    file_name = f"./financialData/{company.lower()}_stock_data.csv"
    history.to_csv(file_name)

    print(f"Data for {company} saved to {file_name}")

print("Download complete.")
