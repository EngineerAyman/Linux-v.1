'''
NumPy Module:
The NumPy module is used for numerical computations in Python.
 Here's an example code for performing matrix multiplication using NumPy:

'''


import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = np.dot(A, B)

print(C)