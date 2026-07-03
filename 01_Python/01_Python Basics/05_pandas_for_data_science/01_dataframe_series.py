import pandas as pd

#series = one column

marks = pd.Series([85, 90, 78, 92])

print("Marks Series")
print (marks)


#Dataframe = table

students = pd.DataFrame({
    "name" : ["Neelam", "Aarav", "Priya", "John"],
    "marks": [85, 90, 78, 92],
    "attendance": [92, 88, 75, 95],
    "course": ["ML", "AI", "Data Science", "ML"]
})


print("\nStudents DataFrame:")
print(students)

print("\nFirst 2 rows:")
print(students.head(2))

print("\nDataFrame shape:")
print(students.shape)

print("\nColumn names:")
print(students.columns)

print("\nBasic information:")
print(students.info())

print("\nSummary statistics:")
print(students.describe())