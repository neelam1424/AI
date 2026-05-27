import pandas as pd

df = pd.read_csv("data/students.csv")

print("Original Data:")
print(df)

# Select one column
print("\nNames:")
print(df["name"])

# Select multiple columns
print("\nName and Marks:")
print(df[["name", "marks"]])

# Filter students with marks >= 85
high_scores = df[df["marks"] >= 85]

print("\nHigh Score Students:")
print(high_scores)

# Filter students from New Jersey
nj_students = df[df["city"] == "New Jersey"]

print("\nNew Jersey Students:")
print(nj_students)

# Multiple conditions
good_students = df[(df["marks"] >= 80) & (df["attendance"] >= 85)]

print("\nGood Students:")
print(good_students)

# loc: label-based
print("\nUsing loc:")
print(df.loc[0, "name"])

# iloc: position-based
print("\nUsing iloc:")
print(df.iloc[0, 1])

# Select rows and columns using loc
print("\nloc rows 0 to 2, selected columns:")
print(df.loc[0:2, ["name", "marks"]])

# Select rows and columns using iloc
print("\niloc first 3 rows, columns 1 to 3:")
print(df.iloc[0:3, 1:4])