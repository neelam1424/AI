import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/students.csv")

numeric_df = df[["marks", "attendance", "study_hours"]]

correlation = numeric_df.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.xlabel("Course")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

sns.pairplot(numeric_df)
plt.show()