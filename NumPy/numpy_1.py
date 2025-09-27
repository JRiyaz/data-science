import sys

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(sys.getsizeof(arr))
print(arr)
print("Array shape:", arr.shape)
print("Array data type:", arr.dtype)
print("Array sum:", arr.sum())
print(arr.nbytes)


# print(sys.getsizeof(arr))  # Size of the list object

# Non zero
arr = np.array([0, 2, 0, 0, 5])
arr_non_zero = np.nonzero(arr)
print(arr_non_zero)
