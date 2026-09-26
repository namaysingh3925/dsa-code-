r = int(input("Enter number of rows: "))
c = int(input("Enter number of cols: "))

print("Enter Matrix A:")
A, B, C, D = [], [], [], []

for i in range(r):
    temp = []
    for j in range(c):
        temp.append(int(input("Enter the value: ")))
    A.append(temp)

print("Enter Matrix B:")
for i in range(r):
    temp = []
    for j in range(c):
        temp.append(int(input("Enter the value: ")))
    B.append(temp)
for i in range(r):
    t_a, t_s = [], []
    for j in range(c):
        t_a.append(A[i][j] + B[i][j])
        t_s.append(A[i][j] - B[i][j])
    C.append(t_a)
    D.append(t_s)

print("Matrix A:")
for i in range(r):
    print(A[i])

print("Matrix B:")
for i in range(r):
    print(B[i])

print("Addition Matrix:")
for i in range(r):
    print(C[i])

print("Subtraction Matrix:")
for i in range(r):
    print(D[i])
