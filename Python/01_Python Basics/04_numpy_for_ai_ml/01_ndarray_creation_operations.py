import numpy as np


# creating a 1D NumPy array

marks=np.array([80,85,90,95])


print("Marks", marks)
print("Type: ",type(marks))


#operation on the full array

print("Add 5 bonus marks: ", marks+5)
print("Double marks", marks * 2)


#Useful statistics

print("Average marks: ", np.mean(marks))
print("Highest marks", np.max(marks))
print("Lowest marks: ",np.min(marks))


# creating a 2D array

student_scores = np.array([
    [80, 85, 90],
    [70, 75, 78],
    [88, 92, 95],
])

print("Student Scores:")
print(student_scores)

print("Shape:", student_scores.shape)
print("Rows and columns:", student_scores.shape)