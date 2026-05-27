import numpy as np

#create array

features=np.array([
    [1.2, 3.4, 5.6],
    [2.1, 4.3, 6.5],
    [3.2, 5.4, 7.6]
])

print("Original features:")
print(features)

#save array
np.save("features.npy", features)

print("Array saved as features.npy")


# Load array
loaded_features = np.load("features.npy")



print("Loaded features:")
print(loaded_features)