import pandas as pd
import numpy as np

# Step 1: Create student dataset
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Neelam", "Aarav", "Priya", "John", "Sara", "Mike", "Ananya"],
    "course": ["ML", "AI", "Data Science", "ML", "AI", "ML", "Data Science"],
    "marks": [85, 90, 78, 92, np.nan, 80, 89],
    "attendance": [92, 88, 75, 95, 70, np.nan, 91],
    "city": ["New Jersey", "New York", "Boston", "Chicago", "New Jersey", "Dallas", "Seattle"]
})

print("Original Student Data:")
print(students)

# Step 2: Check missing values
print("\nMissing Values:")
print(students.isnull().sum())

# Step 3: Fill missing numerical values
students["marks"] = students["marks"].fillna(students["marks"].mean())
students["attendance"] = students["attendance"].fillna(students["attendance"].median())

print("\nAfter Handling Missing Values:")
print(students)

# Step 4: Create result column
students["result"] = students["marks"].map(lambda mark: "Pass" if mark >= 60 else "Fail")

# Step 5: Create performance column
def assign_performance(row):
    if row["marks"] >= 85 and row["attendance"] >= 85:
        return "Excellent"
    elif row["marks"] >= 75:
        return "Good"
    else:
        return "Needs Improvement"

students["performance"] = students.apply(assign_performance, axis=1)

print("\nAfter Adding Result and Performance:")
print(students)

# Step 6: Group by course
course_summary = students.groupby("course").agg({
    "marks": ["mean", "max", "min"],
    "attendance": "mean",
    "student_id": "count"
})

print("\nCourse Summary:")
print(course_summary)

# Step 7: Create course details table
courses = pd.DataFrame({
    "course": ["ML", "AI", "Data Science"],
    "instructor": ["Dr. Smith", "Dr. Brown", "Dr. Lee"],
    "credits": [3, 3, 4]
})

# Step 8: Merge student data with course data
final_data = pd.merge(students, courses, on="course", how="left")

print("\nFinal Merged Data:")
print(final_data)

# Step 9: Save final cleaned data
final_data.to_csv("cleaned_student_performance.csv", index=False)

print("\nCleaned data saved as cleaned_student_performance.csv")