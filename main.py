import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

# Step 1: Load the dataset
url = "https://raw.githubusercontent.com/datasets/housing-prices/main/data.csv"  # Replace this with the Kaggle dataset path if needed
data = pd.read_csv(url)

# Simplify dataset to include a few features for beginners
selected_features = ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "YearBuilt", "SalePrice"]
data = data[selected_features]

# Drop rows with missing values
data.dropna(inplace=True)

# Step 2: Split data into features (X) and target (y)
X = data.drop("SalePrice", axis=1)
y = data["SalePrice"]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model trained. Mean Absolute Error on test data: ${mae:.2f}")

# Step 6: User input for predictions
def predict_house_price():
    print("\nEnter the following details about the house:")
    overall_qual = int(input("Overall Quality (1-10): "))
    gr_liv_area = int(input("Above Ground Living Area (in square feet): "))
    garage_cars = int(input("Number of Cars the Garage Can Fit: "))
    total_bsmt_sf = int(input("Total Basement Area (in square feet): "))
    year_built = int(input("Year the House was Built: "))
    
    # Create input array and predict
    input_data = np.array([[overall_qual, gr_liv_area, garage_cars, total_bsmt_sf, year_built]])
    predicted_price = model.predict(input_data)[0]
    print(f"\nThe predicted house price is: ${predicted_price:.2f}")

# Allow user to make predictions
predict_house_price()
