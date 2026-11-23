import numpy as np
marks = list(map(int,input("Enter your marks: ").split()))
print(marks)

arr = np.array(marks)
print("Mean:",np.mean(arr))
print("Median:",np.median(arr))
print("Standard Deviation:",np.std(arr))
print("Maximum:",np.max(arr))
print("Minimum",np.min(arr))