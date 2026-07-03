import pandas as pd

df = pd.read_csv("data/sales.csv")

import pandas as pd

df = pd.read_csv("data/sales.csv")

print("Original Data:")
print(df)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Set date as index
df = df.set_index("date")

print("\nData with Date Index:")
print(df)

# Resample daily data into weekly total sales
weekly_sales = df.resample("W").sum()

print("\nWeekly Sales:")
print(weekly_sales)


# Rolling 3-day average

df["rolling_3_day_avg"] = df["sales"].rolling(window=3).mean()

print("\nSales with Rolling Average:")
print(df)