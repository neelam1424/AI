import numpy as np

#rreshapin
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped = arr.reshape(2,3)

print("Original array:")
print(arr)

print("Reshaped array:")
print(reshaped)


#slicing 1D array

scores = np.array([70,80,85,90,95])


print("First score: ", scores[0])
print("Middle score: ", scores[1:4])
print("First three scores:", scores[:3])


# 2D slicing
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("First row", data[0])



print("First column:")
print(data[:, 0])


print("Bottom-right section:")
print(data[1:, 1:])


# Fancy indexing
selected_rows = data[[0, 2]]

print("Selected rows:")
print(selected_rows)