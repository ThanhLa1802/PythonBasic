import numpy as np

#init array from list
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1d)
print("2D Array:\n", arr2d)

zeros_arr = np.zeros((2, 3))
ones_arr = np.ones((3, 2))
print("Zeros Array:\n", zeros_arr)
print("Ones Array:\n", ones_arr)