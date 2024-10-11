def identify_and_clean_column(series):
    """Identifies and cleans non-numeric types in a Pandas Series."""
    for i, value in enumerate(series):
        if not isinstance(value, (int, float)):
            print(
                f"Non-numeric value at index {i}: {value} (type: {type(value)})")

    # Convert the series to numeric, coercing errors to NaN
    cleaned_series = pd.to_numeric(series, errors='coerce')
    return cleaned_series


def layoffs_by_quarter_year(df):
    # Identify and clean 'total_laid_off' column
    df['total_laid_off'] = identify_and_clean_column(df['total_laid_off'])

    # Drop rows with NaN values in 'total_laid_off'
    df.dropna(subset=['total_laid_off'], inplace=True)

    # Convert date column to datetime and extract quarter
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)
    df['quarter'] = df['date'].dt.to_period('Q')

    # Aggregate layoffs by quarter
    layoffs = df.groupby(['quarter']).agg(
        {'total_laid_off': 'sum'}).reset_index()

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=layoffs, x='quarter', y='total_laid_off', marker='o')
    plt.title('Total Layoffs by Quarter')
    plt.xlabel('Quarter')
    plt.ylabel('Total Layoffs')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("layoffs_by_quarter_year.png")
    plt.show()