import numpy as np
import time

#large dataset

numbers=np.arrange(1, 1_000_001)


start_time = time.time()

squares_loop = []

for number in numbers:
    squares_loop.append(number * number)

end_time= time.time()



print("Loop time: ", end_time -start_time)


# vectorized method


start_time = time.time()

squared_vectorized = numbers * numbers

end_time = time.time()

print("Vectorized time: ", end_time - start_time)


