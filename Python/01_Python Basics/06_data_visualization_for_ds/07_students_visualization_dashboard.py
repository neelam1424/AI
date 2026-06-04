import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/students.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())

plt.figure(figsize=(8, 5))
sns.histplot(df["marks"], bins=6, kde=True)
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("charts/marks_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="course", y="marks")
plt.title("Marks Distribution by Course")
plt.xlabel("Course")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("charts/course_marks_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="study_hours", y="marks", hue="course", s=100)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("charts/study_hours_vs_marks.png", dpi=300, bbox_inches="tight")
plt.show()

numeric_df = df[["marks", "attendance", "study_hours"]]

plt.figure(figsize=(6, 4))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("charts/correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

course_avg = df.groupby("course")["marks"].mean().reset_index()

plt.figure(figsize=(7, 4))
sns.barplot(data=course_avg, x="course", y="marks")
plt.title("Average Marks by Course")
plt.xlabel("Course")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("charts/average_marks_by_course.png", dpi=300, bbox_inches="tight")
plt.show()

fig = px.scatter(
    df,
    x="study_hours",
    y="marks",
    color="course",
    size="attendance",
    hover_data=["name", "city"],
    title="Interactive Student Performance Dashboard"
)

fig.write_html("charts/interactive_student_dashboard.html")

print("\nAll charts saved inside the charts folder.")