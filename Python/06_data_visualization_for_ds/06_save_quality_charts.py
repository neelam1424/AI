import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/students.csv")

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="name", y="marks")
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/student_marks.png", dpi=300, bbox_inches="tight")

plt.show()

numeric_df = df[["marks", "attendance", "study_hours"]]

plt.figure(figsize=(6, 4))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("charts/correlation_heatmap.png", dpi=300, bbox_inches="tight")

plt.show()