import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/students.csv")


print(df.head())


plt.figure(figsize=(8, 5))

plt.bar(df["name"], df["marks"])

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

