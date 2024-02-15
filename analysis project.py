from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
file_path = 'your_output_file2.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)


# Assuming you have a DataFrame df with features and labels
X = df.drop(columns=['School_University_in_Township', 'Hospital_in_TownShip', 'Mall_in_TownShip', 'Park_Jogging_track', 'Swimming_Pool', 'Gym'])
y = df['School_University_in_Township', 'Hospital_in_TownShip', 'Mall_in_TownShip', 'Park_Jogging_track', 'Swimming_Pool', 'Gym']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now, you can use LabelEncoder to encode categorical labels if needed
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)
print(y_test_encoded)
print(y_train_encoded)