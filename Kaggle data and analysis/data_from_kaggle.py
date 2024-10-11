# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("swaptr/layoffs-2022")

# print("Path to dataset files:", path)


import pandas as pd


# def load_and_prepare_data(file_path):
#     # Load the CSV file
#     df = pd.read_csv(file_path)

#     # Convert 'date' column to datetime format
#     df['date'] = pd.to_datetime(df['date'], errors='coerce')

#     # Drop rows with NaT (Not a Time) in 'date' column due to conversion errors
#     df = df.dropna(subset=['date'])

#     # Extract year and quarter from the date
#     df['year'] = df['date'].dt.year
#     df['quarter'] = df['date'].dt.to_period('Q')

#     # Ensure 'total_laid_off' is numeric (replace non-numeric values with NaN and then fill them with 0)
#     df['total_laid_off'] = pd.to_numeric(
#         df['total_laid_off'], errors='coerce').fillna(0)

#     return df


# def group_by_company_and_quarter(df):
#     # Group by company, year, and quarter, then sum 'total_laid_off'
#     grouped_df = df.groupby(['company', 'year', 'quarter'])[
#         'total_laid_off'].sum().reset_index()

#     # Rename columns for clarity
#     grouped_df.columns = ['Company', 'Year', 'Quarter', 'Total_Laid_Off']

#     return grouped_df


# def save_to_csv(df, output_file_path):
#     # Save the grouped data to a new CSV file
#     df.to_csv(output_file_path, index=False)


# # Example usage
# file_path = 'layoffs.csv'  # Replace with the path to your CSV file
# # Replace with your desired output file path
# output_file_path = 'filtered_and_grouped_data.csv'

# # Load, process, group, and save the data
# df = load_and_prepare_data(file_path)
# layoffs_by_quarter = group_by_company_and_quarter(df)
# save_to_csv(layoffs_by_quarter, output_file_path)

# print(f"Grouped data saved to {output_file_path}")


# import pandas as pd


# def load_data(file_path):
#     return pd.read_csv(file_path)


# def layoffs_by_quarter_year(df):
#     df['date'] = pd.to_datetime(df['date'])
#     df['year'] = df['date'].dt.year
#     df['quarter'] = df['date'].dt.to_period('Q')
#     layoffs = df.groupby(['year', 'quarter'])[
#         'total_laid_off'].sum().reset_index()
#     return layoffs


# def layoffs_by_industry(df):
#     layoffs_industry = df.groupby(
#         'industry')['total_laid_off'].sum().reset_index()
#     return layoffs_industry.sort_values(by='total_laid_off', ascending=False)


# def layoffs_by_country(df):
#     layoffs_country = df.groupby(
#         'country')['total_laid_off'].sum().reset_index()
#     return layoffs_country.sort_values(by='total_laid_off', ascending=False)


# def average_layoffs_per_company(df):
#     avg_layoffs = df.groupby('company')['total_laid_off'].mean().reset_index()
#     return avg_layoffs.sort_values(by='total_laid_off', ascending=False)


# def layoffs_by_stage(df):
#     layoffs_stage = df.groupby('stage')['total_laid_off'].sum().reset_index()
#     return layoffs_stage.sort_values(by='total_laid_off', ascending=False)


# def top_companies_by_layoffs(df, top_n=10):
#     total_layoffs_company = df.groupby(
#         'company')['total_laid_off'].sum().reset_index()
#     return total_layoffs_company.sort_values(by='total_laid_off', ascending=False).head(top_n)


# def layoffs_by_funding(df):
#     bins = [0, 10, 100, 1000, 10000, float('inf')]
#     labels = ['0-10M', '10-100M', '100M-1B', '1B-10B', '10B+']
#     df['funds_raised_bin'] = pd.cut(
#         df['funds_raised'], bins=bins, labels=labels)
#     layoffs_funding = df.groupby('funds_raised_bin')[
#         'total_laid_off'].sum().reset_index()
#     return layoffs_funding.sort_values(by='total_laid_off', ascending=False)


# def percentage_layoffs_by_industry(df):
#     total_layoffs = df['total_laid_off'].sum()
#     layoffs_industry = df.groupby(
#         'industry')['total_laid_off'].sum().reset_index()
#     layoffs_industry['percentage'] = (
#         layoffs_industry['total_laid_off'] / total_layoffs) * 100
#     return layoffs_industry.sort_values(by='percentage', ascending=False)


# def correlation_funds_layoffs(df):
#     correlation = df[['funds_raised', 'total_laid_off']].corr()
#     return correlation


# # Load data
# file_path = 'layoffs.csv'
# df = load_data(file_path)

# # Analyze layoffs by quarter and year
# print(layoffs_by_quarter_year(df))

# # Analyze layoffs by industry
# print(layoffs_by_industry(df))

# # Check correlation between funds raised and layoffs
# print(correlation_funds_layoffs(df))

#####################################################################################################################################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data


def load_data(file_path):
    return pd.read_csv(file_path)

# Calculate Layoffs by Quarter and Year


def layoffs_by_quarter_year(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['quarter'] = df['date'].dt.to_period('Q')
    layoffs = df.groupby(['year', 'quarter'])[
        'total_laid_off'].sum().reset_index()
    layoffs.to_csv('layoffs_by_quarter_year.csv', index=False)

#     # Load the data from a CSV file
# # Ensure the CSV file has headers: "year", "quarter", "total_laid_off"
# df = pd.read_csv('layoffs_by_quarter_year.csv')

# # Plot the data
# plt.figure(figsize=(10, 6))
# plt.plot(df['quarter'], df['total_laid_off'],
#          marker='o', color='b', linestyle='-')
# plt.xticks(rotation=45)
# plt.xlabel('Quarter')
# plt.ylabel('Total Laid Off')
# plt.title('Total Layoffs by Quarter')
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.lineplot(data=layoffs, x='quarter', y='total_laid_off', marker='o')
# plt.title('Total Layoffs by Quarter and Year')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.savefig('layoffs_by_quarter_year.png')
# plt.show()


# Layoffs by Industry


def layoffs_by_industry(df):
    layoffs_industry = df.groupby(
        'industry')['total_laid_off'].sum().reset_index()
    layoffs_industry.to_csv('layoffs_by_industry.csv', index=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=layoffs_industry, x='total_laid_off',
                y='industry', palette='viridis')
    plt.title('Total Layoffs by Industry')
    plt.tight_layout()
    plt.savefig('layoffs_by_industry.png')
    plt.show()

# Layoffs by Country


def layoffs_by_country(df):
    layoffs_country = df.groupby(
        'country')['total_laid_off'].sum().reset_index()
    layoffs_country.to_csv('layoffs_by_country.csv', index=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=layoffs_country, x='total_laid_off',
                y='country', palette='magma')
    plt.title('Total Layoffs by Country')
    plt.tight_layout()
    plt.savefig('layoffs_by_country.png')
    plt.show()

# Average Layoffs per Company


def average_layoffs_per_company(df):
    avg_layoffs = df.groupby('company')['total_laid_off'].mean().reset_index()
    avg_layoffs.to_csv('average_layoffs_per_company.csv', index=False)

    plt.figure(figsize=(12, 6))
    top_avg = avg_layoffs.sort_values(
        by='total_laid_off', ascending=False).head(10)
    sns.barplot(data=top_avg, x='total_laid_off',
                y='company', palette='coolwarm')
    plt.title('Top 10 Companies by Average Layoffs')
    plt.tight_layout()
    plt.savefig('average_layoffs_per_company.png')
    plt.show()

# Layoffs by Stage


def layoffs_by_stage(df):
    layoffs_stage = df.groupby('stage')['total_laid_off'].sum().reset_index()
    layoffs_stage.to_csv('layoffs_by_stage.csv', index=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=layoffs_stage, x='total_laid_off',
                y='stage', palette='plasma')
    plt.title('Total Layoffs by Company Stage')
    plt.tight_layout()
    plt.savefig('layoffs_by_stage.png')
    plt.show()

# Layoffs by Funding Raised


def layoffs_by_funding(df):
    bins = [0, 10, 100, 1000, 10000, float('inf')]
    labels = ['0-10M', '10-100M', '100M-1B', '1B-10B', '10B+']
    df['funds_raised_bin'] = pd.cut(
        df['funds_raised'], bins=bins, labels=labels)
    layoffs_funding = df.groupby('funds_raised_bin')[
        'total_laid_off'].sum().reset_index()
    layoffs_funding.to_csv('layoffs_by_funding.csv', index=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=layoffs_funding, x='funds_raised_bin',
                y='total_laid_off', palette='cividis')
    plt.title('Total Layoffs by Funding Raised')
    plt.tight_layout()
    plt.savefig('layoffs_by_funding.png')
    plt.show()

# Percentage of Layoffs by Industry


def percentage_layoffs_by_industry(df):
    total_layoffs = df['total_laid_off'].sum()
    layoffs_industry = df.groupby(
        'industry')['total_laid_off'].sum().reset_index()
    layoffs_industry['percentage'] = (
        layoffs_industry['total_laid_off'] / total_layoffs) * 100
    layoffs_industry.to_csv('percentage_layoffs_by_industry.csv', index=False)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=layoffs_industry, x='percentage',
                y='industry', palette='rocket')
    plt.title('Percentage of Layoffs by Industry')
    plt.tight_layout()
    plt.savefig('percentage_layoffs_by_industry.png')
    plt.show()

# Correlation Between Funds Raised and Layoffs


def correlation_funds_layoffs(df):
    correlation = df[['funds_raised', 'total_laid_off']].corr()
    correlation.to_csv('correlation_funds_layoffs.csv')

    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Funds Raised and Total Layoffs')
    plt.tight_layout()
    plt.savefig('correlation_funds_layoffs.png')
    plt.show()

# Run all analyses


def run_analysis(file_path):
    df = load_data(file_path)
    layoffs_by_quarter_year(df)
    layoffs_by_industry(df)
    layoffs_by_country(df)
    average_layoffs_per_company(df)
    layoffs_by_stage(df)
    layoffs_by_funding(df)
    percentage_layoffs_by_industry(df)
    correlation_funds_layoffs(df)


# Example usage
file_path = 'layoffs.csv'  # Replace with your file path
run_analysis(file_path)
