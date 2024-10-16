import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the CSV data
data = pd.read_csv('final-merged-dataset-with-layoff-indicator.csv')

# Filter data for a specific company
company_name = 'Google'  # replace with the company name you want to focus on
company_data = data[data['company_name'] == company_name]

# Save filtered data to a new CSV file
company_csv_file = f"{company_name}_data.csv"
company_data.to_csv(company_csv_file, index=False)
print(f"Filtered data saved to {company_csv_file}")

# Define features (X) and target (y)
# Selecting relevant columns for model training
features = ['open', 'high', 'low', 'close', 'volume',
            'changePercent', 'marketCap', 'sma', 'rsi', 'adx']
X = company_data[features]
y = company_data['layoff']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Example of saving the trained model for future predictions
model_filename = f"{company_name}_layoff_predictor_model.pkl"
joblib.dump(model, model_filename)
print(f"Trained model saved to {model_filename}")
