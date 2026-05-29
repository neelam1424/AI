import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/students.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

plt.figure(figsize=(7, 4))
sns.histplot(df["marks"], bins=5, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

numeric_df = df[["marks", "attendance", "study_hours"]]
correlation = numeric_df.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Feature Correlation")
plt.tight_layout()
plt.show()