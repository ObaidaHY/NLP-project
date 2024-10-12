from yahooquery import search
import yfinance as yf


def get_financial_data():
    # List of company tickers
    tickers = {
        # Note: You will only get historical data for Twitter before the acquisition.
        'Twitter': 'TWTR'
    }

    # Define start and end dates for the time period you want
    start_date = '2010-01-01'
    end_date = '2024-04-15'

    # Iterate through each company and download historical stock data
    for company, ticker in tickers.items():
        print(f"Downloading data for {company} ({ticker})...")

        # Get historical stock data for the company
        stock_data = yf.Ticker(ticker)
        history = stock_data.history(
            start=start_date, end=end_date, interval='1mo')  # Monthly data

        # Save the historical data to a CSV file
        file_name = f"./financialData/{company.lower()}_stock_data.csv"
        history.to_csv(file_name)

        print(f"Data for {company} saved to {file_name}")

    print("Download complete.")


# Import yahooquery for searching ticker symbols


def get_ticker(company_name):
    # Search for the company name
    results = search(company_name)
    # Check if any results were found
    if results['quotes']:
        # Return the first result's symbol
        print(results)
        return results['quotes'][0]['symbol']
    else:
        return None


# Example usage
company_name = "Apple"
ticker = get_ticker(company_name)
if ticker:
    print(f"The ticker for {company_name} is {ticker}.")
else:
    print(f"No ticker found for {company_name}.")
