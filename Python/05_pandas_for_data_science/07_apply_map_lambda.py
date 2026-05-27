import pandas as pd

df = pd.read_csv("data/students.csv")

print("Original Data:")
print(df)

# map with lambda
df["result"] = df["marks"].map(lambda mark: "Pass" if mark >= 60 else "Fail")

print("\nAfter Result Column:")
print(df)

# apply with function
def assign_performance(row):
    if row["marks"] >= 85 and row["attendance"] >= 85:
        return "Excellent"
    elif row["marks"] >= 70:
        return "Good"
    else:
        return "Needs Improvement"


df["performance"] = df.apply(assign_performance, axis=1)

print("\nAfter Performance Column:")
print(df)

# Create email username using lambda
df["email_username"] = df["name"].map(lambda name: name.lower() + "@student.com")

print("\nAfter Email Username Column:")
print(df[["name", "email_username"]])