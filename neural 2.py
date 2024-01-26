import numpy as np

# Create a random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Replace the max in each row by 0 along axis=1
reshaped_array[np.arange(reshaped_array.shape[0]), reshaped_array.argmax(axis=1)] = 0

print(reshaped_array)