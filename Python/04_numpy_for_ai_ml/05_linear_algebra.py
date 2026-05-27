import numpy as np

# Feature vector
features = np.array([1, 2, 3])

# Weight vector
weights = np.array([0.2, 0.5, 0.3])

# Dot product
prediction = np.dot(features, weights)

print("Prediction using dot product:", prediction)

# Matrix multiplication
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

matrix_result = A @ B

print("Matrix Multiplication Result:")
print(matrix_result)

# Determinant
determinant = np.linalg.det(A)

print("Determinant of A:", determinant)

# Inverse
inverse = np.linalg.inv(A)

print("Inverse of A:")
print(inverse)

# Norm
vector = np.array([3, 4])

norm = np.linalg.norm(vector)

print("Vector norm:", norm)