import numpy as np


# Seed makes randomness reproducible
np.random.seed(42)



# Uniform random values between 0 and 1

uniform_values = np.random.uniform(0, 1, 5)

print("Uniform values:")
print(uniform_values)


# Normal random values with mean 0 and std 1
normal_values = np.random.normal(0, 1, 5)


print("Normal values:")
print(normal_values)


# Random dataset: 5 rows, 3 columns

synthetic_data = np.random.normal(50, 10, size=(5,3))

print("Synthetic student-like data:")
print(synthetic_data)