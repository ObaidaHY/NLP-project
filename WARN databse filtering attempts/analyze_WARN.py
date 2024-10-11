import pandas as pd

# # Load data from Excel file


# def load_data(file_path):
#     df = pd.read_excel(file_path)
#     return df

# # Group information by company


# def group_by_company(df):
#     grouped_df = df.groupby('Company').agg({
#         'State': 'first',
#         'City': 'first',
#         'Number of Workers': 'sum',
#         'WARN Received Date': 'first',
#         'Effective Date': 'first',
#         'Closure/Layoff': 'first',
#         'Temporary/Permanent': 'first',
#         'Union': 'first',
#         'Region': 'first',
#         'County': 'first',
#         'Industry': 'first',
#         'Notes': 'first'
#     }).reset_index()
#     return grouped_df

# # Find years with the most layoffs


# def layoffs_by_year(df):
#     df['Year'] = pd.to_datetime(df['WARN Received Date']).dt.year
#     year_summary = df.groupby(
#         'Year')['Number of Workers'].sum().sort_values(ascending=False)
#     return year_summary

# # Analyze other trends


# def analyze_other_trends(df):
#     # Example: Trends by industry
#     industry_trends = df.groupby(
#         'Industry')['Number of Workers'].sum().sort_values(ascending=False)

#     # Example: Trends by closure/layoff type
#     closure_layoff_trends = df.groupby(
#         'Closure/Layoff')['Number of Workers'].sum()

#     return industry_trends, closure_layoff_trends


# # Example usage
# file_path = "C:/Users/obayd/Downloads/WARN-Database.xlsx"
# df = load_data(file_path)
# company_data = group_by_company(df)
# layoffs_by_year_data = layoffs_by_year(df)
# industry_trends, closure_layoff_trends = analyze_other_trends(df)

# print(company_data.head())
# print(layoffs_by_year_data)
# print(industry_trends)
# print(closure_layoff_trends)


# # Load data from Excel file and write unique company names to a text file with UTF-8 encoding
# def save_unique_companies_to_file(file_path, output_file):
#     df = pd.read_excel(file_path)
#     unique_companies = df['Company'].unique()

#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write("Unique Companies:\n")
#         for company in unique_companies:
#             f.write(f"{company}\n")


# # Example usage
# file_path = "C:/Users/obayd/Downloads/WARN-Database.xlsx"
# output_file = 'unique_companies.txt'
# save_unique_companies_to_file(file_path, output_file)
# print(f"Unique company names have been saved to {output_file}")


# Function to get a unique list of companies with the highest number of layoffs
import numpy as np

# Function to get a unique list of companies with the highest number of layoffs


# def get_top_companies(file_path, num_companies=50):
#     df = pd.read_excel(file_path)

#     # Ensure that 'Number of Workers' column is numeric, coerce errors to NaN
#     df['Number of Workers'] = pd.to_numeric(
#         df['Number of Workers'], errors='coerce')

#     # Drop rows where 'Number of Workers' is NaN after conversion
#     df = df.dropna(subset=['Number of Workers'])

#     # Group by company and sum the number of layoffs
#     company_layoffs = df.groupby('Company')['Number of Workers'].sum()

#     # Sort companies by total layoffs in descending order and select the top ones
#     top_companies = company_layoffs.sort_values(
#         ascending=False).head(num_companies)

#     return list(top_companies.index)


# # Example usage
# file_path = "C:/Users/obayd/Downloads/WARN-Database.xlsx"
# selected_companies = get_top_companies(file_path)
# print(f"Selected companies for LLM training:\n{selected_companies}")


# import pandas as pd


# def remove_closure_rows(input_file, output_file):
#     # Load the Excel file into a DataFrame
#     df = pd.read_excel(input_file)

#     # Filter out rows where the 'Closure/Layoff' column contains the word 'closure'
#     filtered_df = df[~df['Closure/Layoff']
#                      .str.contains('clos', case=False, na=False)]

#     # Save the filtered DataFrame to a new Excel file
#     filtered_df.to_excel(output_file, index=False)


# # Example usage
# # Replace with your input file path
# input_file = "C:/Users/obayd/Downloads/WARN-Database.xlsx"
# # Replace with your desired output file path
# output_file = 'without_closure.xlsx'

# remove_closure_rows(input_file, output_file)

def get_years_with_lots_of_layoffs(input_file, threshold):
    # Load the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Convert 'Effective Date' to datetime format if not already
    df['Effective Date'] = pd.to_datetime(
        df['Effective Date'], errors='coerce')

    # Extract year from 'Effective Date'
    df['Year'] = df['Effective Date'].dt.year

    # Convert 'Number of Workers' to numeric, coercing errors to NaN
    df['Number of Workers'] = pd.to_numeric(
        df['Number of Workers'], errors='coerce')

    # Drop rows with NaN values in 'Number of Workers' (or fill them with 0)
    df = df.dropna(subset=['Number of Workers'])

    # Group by year and sum the number of layoffs
    layoffs_by_year = df.groupby(
        'Year')['Number of Workers'].sum().reset_index()

    # Filter years with layoffs above the specified threshold
    significant_layoffs = layoffs_by_year[layoffs_by_year['Number of Workers'] > threshold]

    return significant_layoffs


# Example usage
input_file = 'without_closure.xlsx'  # Replace with your input file path
threshold = 1000                          # Define a threshold for significant layoffs

years_with_lots_of_layoffs = get_years_with_lots_of_layoffs(
    input_file, threshold)
print(years_with_lots_of_layoffs)

''' 
result : 
0   1996.0             3398.0
1   1997.0            20124.0
2   1998.0            40336.0
3   1999.0            34600.0
4   2000.0            35751.0
5   2001.0           104970.0
6   2002.0            77027.0
7   2003.0            65643.0
8   2004.0            83424.0
9   2005.0            86334.0
10  2006.0            88543.0
11  2007.0            86461.0
12  2008.0           151103.0
13  2009.0           183661.0
14  2010.0            96165.0
15  2011.0           100473.0
16  2012.0           115552.0
17  2013.0           100156.0
18  2014.0           141942.0
19  2015.0           178381.0
20  2016.0           159850.0
21  2017.0           147032.0
22  2018.0           146569.0
23  2019.0           147121.0
24  2020.0          1799197.0
25  2021.0           122000.0
26  2022.0            92249.0
27  2023.0           198637.0
28  2024.0            54350.0
'''
