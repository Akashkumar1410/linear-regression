import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import precision_score, recall_score, classification_report

# Load your Excel file
file_path = "your_output_file2.xlsx"
df = pd.read_excel(file_path)

# Assuming 'Price_in_lakhs' is your continuous target variable
threshold = 20  # Example threshold, adjust as needed
df['Price_Class'] = (df['Price_in_lakhs'] > threshold).astype(int)

# Select features (independent variables) and the target variable
columns_to_exclude = ['Price_in_lakhs', 'Mall_in_TownShip', 'Sub_Area', 'ClubHouse', 'School_University_in_Township', 'Hospital_in_TownShip', 'Park_Jogging_track', 'Swimming_Pool', 'Gym']
X = df.drop(columns_to_exclude + ['Price_Class'], axis=1)  # Independent variables
y = df['Price_Class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = (model.predict(X_test) > threshold).astype(int)

# Evaluate the classification model
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f'Precision: {precision}')
print(f'Recall: {recall}')

# Additional classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))
