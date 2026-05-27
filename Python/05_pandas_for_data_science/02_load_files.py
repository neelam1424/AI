import pandas as pd

import sqlite3


#load csv

students_csv = pd.read_csv("data/students.csv")

print("CSV Data:")
print(students_csv)

#create JSON-like data manually

courses = pd.DataFrame({
    "course": ["ML", "AI", "Data Science"],
    "instructor": ["Dr. Smith", "Dr. Brown", "Dr. Lee"],
    "credits": [3, 3, 4]
})

courses.to_json("data/courses.json", orient="records")

# Load JSON file
courses_json = pd.read_json("data/courses.json")

print("\nJSON Data:")
print(courses_json)


# SQL example using SQLite
connection = sqlite3.connect("students.db")

students_csv.to_sql("students", connection, if_exists="replace", index=False)

students_sql = pd.read_sql_query("SELECT * FROM students", connection)

print("\nSQL Data:")
print(students_sql)

connection.close()