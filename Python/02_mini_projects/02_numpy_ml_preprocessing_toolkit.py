import numpy as np


np.random.seed(42)

# Step 1: Create synthetic dataset
# 10 students, 3 features: study_hours, attendance, previous_score
data = np.array([
    [5, 80, 70],
    [3, 60, 55],
    [8, 90, 85],
    [2, 50, 40],
    [7, 85, 78],
    [6, 75, 72],
    [4, 65, 60],
    [9, 95, 92],
    [1, 40, 35],
    [10, 98, 96]
])


print("Original data: ")
print(data)


study_hours = data[:, 0]
attendance = data[:, 1]
previous_score= data[:, 2]


mean= np.mean(data, axis=0)
std = np.std(data, axis =0)


normalized_data = (data - mean)/ std


labels = np.where(previous_score >= 70 , "Pass", "Risk")


high_performance_mask = (study_hours>=6) & (attendance >=75)


high_performance= data[high_performance_mask]



weights = np.array([0.3, 0.2, 0.5])


predict_Score = data @ weights


np.save("normalized_student_data.npy", normalized_data)

loaded_data = np.load("normalized_student_data.npy")