import argparse
from datasets import load_dataset
from torch.utils.data import DataLoader
import csv
from tqdm import tqdm
from datetime import datetime
import time 

# Define the target domains
target_domains = ["finance.yahoo.com"]

# Function to check if the URL belongs to one of the target domains
def is_target_domain(url, target_domains):
    return any(domain == url for domain in target_domains)

# Function to check if the published_date is in the specified quarter of the year
def is_in_quarter(date_str, year, quarter):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        quarter_start_end = {
            1: (datetime(year, 1, 1), datetime(year, 3, 31)),
            2: (datetime(year, 4, 1), datetime(year, 6, 30)),
            3: (datetime(year, 7, 1), datetime(year, 9, 30)),
            4: (datetime(year, 10, 1), datetime(year, 12, 31))
        }
        start, end = quarter_start_end[quarter]
        return start <= date <= end
    except ValueError:
        return False  # In case the date is not formatted correctly

# Sequential processing of year-quarter combinations
def process_quarter(year, quarter):
    print(f"Processing data for {year} Q{quarter}")
    
    # Prepare the CSV file for saving
    output_file = f'filtered_q{quarter}_{year}_news.csv'
    
    # Load the CCNews dataset for the specified year
    dataset = load_dataset('stanford-oval/ccnews', name=str(year), split='train', streaming=True)
    
    # Create a DataLoader with prefetching and concurrency
    dataloader = DataLoader(dataset, num_workers=16, prefetch_factor=20, batch_size=None)
    
    start_time = time.time()

    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write the CSV header
        csv_writer.writerow(['publisher', 'published_date', 'plain_text'])

        count = 0
        # Iterate over the streamed dataset and save records from the target domains
        for record in tqdm(dataloader, mininterval=20):
            publisher = record['publisher']
            # Extract relevant fields
            if is_target_domain(publisher, target_domains):
                # Extract relevant fields
                published_date = record['published_date']  # Published date

                # Validate if the published_date is in the specified quarter of the year
                if is_in_quarter(published_date, year, quarter):
                    plain_text = record['plain_text']  # Article content (plain text)
                    # Write the record to the CSV file
                    csv_writer.writerow([publisher, published_date, plain_text])
                    count += 1
                    if count % 1000 == 0:
                        print(f"Processed {count} Articles")

    # Track end time
    end_time = time.time()

    # Calculate and print total time taken
    total_time = end_time - start_time
    print(f"Total time taken for {year} Q{quarter}: {total_time:.2f} seconds")


# Main function to iterate over multiple years and quarters
def main():
    start_year = 2020
    end_year = 2024
    start_quarter = 3
    end_quarter = 2

    # Loop through each year and quarter sequentially
    for year in range(start_year, end_year + 1):
        for quarter in range(start_quarter, end_quarter + 1):
            process_quarter(year, quarter)
            print(f"Finished processing {year} Q{quarter}")

if __name__ == "__main__":
    main()
