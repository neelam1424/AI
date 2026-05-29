import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].bar(df["name"], df["marks"])
axes[0].set_title("Marks")
axes[0].set_xlabel("Students")
axes[0].set_ylabel("Marks")
axes[0].tick_params(axis="x", rotation=45)

axes[1].bar(df["name"], df["attendance"])
axes[1].set_title("Attendance")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Attendance")
axes[1].tick_params(axis="x", rotation=45)

axes[2].scatter(df["study_hours"], df["marks"])
axes[2].set_title("Study Hours vs Marks")
axes[2].set_xlabel("Study Hours")
axes[2].set_ylabel("Marks")

plt.tight_layout()
plt.show()