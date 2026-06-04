import pandas as pd

df = pd.read_csv("data/students.csv")

print("Original Data:")
print(df)


# Average marks by course

average_marks = df.groupby("course")["marks"].mean()

print("\nAverage Marks by Course:")
print(average_marks)


# Multiple aggregations
course_summary = df.groupby("course").agg({
    "marks": ["mean", "max", "min"],
    "attendance": "mean"
})


print("\nCourse Summary:")
print(course_summary)

# Count students per course
student_count = df.groupby("course")["student_id"].count()
print("\nStudent Count by Course:")
print(student_count)


# Pivot table
pivot = pd.pivot_table(
    df,
    values="marks",
    index="course",
    columns="city",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)