A = [[1,2],
     [2,3]]
B = [[2,3],
      [1,2]]
C = [[0,0],
     [0,0]]
D = [[0,0],
     [0,0]]

# addition
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]
print("Addition")
# subtraction

print(C)
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] - B[i][j]
print("Subtraction")
print(C)

# multiplication
for i in range(2):
    for j in range(2):
        for k in range(2):
            D[i][j] += A[i][k]*B[k][j]
print("Multiplication")
print(D)