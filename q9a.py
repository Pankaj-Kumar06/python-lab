import numpy as np
A = np.array([[1,2],
               [3,4]])
B = np.array([[2,1],
              [3,2]])
print("Addition:")
print(A+B)
print("Subtraction:")
print(A - B)
print("Multiplication:")
print(A@B)
print("Transpose")
print(A.T)