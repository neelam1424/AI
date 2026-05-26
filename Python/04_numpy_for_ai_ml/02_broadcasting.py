import numpy as np

# 3 students, 3 subjects

scores = np.array([
    [80, 85, 90],
    [70, 75, 78],
    [88, 92, 95]
])

#Bonus for each subject
bonus= np.array([5, 3, 2])


final_scores = scores + bonus

print("Original scores: \n", scores )


print("Bonus: \n", bonus )

print("Final scores after broadcasting: \n", final_scores )


#ML- like example: normalize data

data = np.array([
    [10,200],
    [20,300],
    [30,400]
])

mean = np.mean(data, axis=0)
std = np.std(data, axis=0)

normalized_data = (data-mean) / std



print("Original Data:")
print(data)

print("Normalized Data:")
print(normalized_data)