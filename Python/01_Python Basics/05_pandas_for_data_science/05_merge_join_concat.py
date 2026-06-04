import pandas as pd

students = pd.read_csv("data/students.csv")


courses = pd.DataFrame({
    "course" : ["ML", "AI", "Data Science"],
    "instrutor" : ["Dr. Smith" , "Dr. Brown", "Dr. Lee"],
    "credits": [3,3,4]
})


print("Students: ",students)

print("\nCourses:")
print(courses)


# Merge students with course details

merged_data =pd.merge(students,courses, on="course", how="left")


print("\nMerged Data:")
print(merged_data)


# Create new batch of students
new_students = pd.DataFrame({
    "student_id": [6, 7],
    "name": ["Mike", "Ananya"],
    "course": ["ML", "AI"],
    "marks": [80, 89],
    "attendance": [85, 91],
    "city": ["Dallas", "Seattle"]
})


# Concatenate old and new students
all_students = pd.concat([students, new_students], ignore_index=True)

print("\nAll Students After Concat:")
print(all_students)