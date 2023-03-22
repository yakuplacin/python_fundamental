import pandas as pd

iowa_file_path = 'train.csv'

home_data = pd.read_csv(iowa_file_path)
print(home_data.columns)
y = home_data.SalePrice

# Create the list of features below
feature_names = ['LotArea', 'YearBuilt', "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]

# Select data corresponding to features in feature_names
X = home_data[feature_names]

print(X.describe())

# print the top few lines
print(X.head())
