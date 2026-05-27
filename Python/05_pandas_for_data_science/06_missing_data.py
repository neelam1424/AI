import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Neelam", "Aarav", "Priya", "John", "Sara"],
    "marks": [85, np.nan, 78, 92, np.nan],
    "attendance": [92, 88, np.nan, 95, 70],
    "city": ["New Jersey", "New York", np.nan, "Chicago", "New Jersey"]
})

print("Original Data with Missing Values:")
print(df)

print("\nMissing value count:")
print(df.isnull().sum())

# Drop rows with missing values
dropped_data = df.dropna()

print("\nAfter dropna:")
print(dropped_data)

# Fill numerical missing values
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())

# Fill categorical missing values
df["city"] = df["city"].fillna(df["city"].mode()[0])

print("\nAfter Imputation:")
print(df)