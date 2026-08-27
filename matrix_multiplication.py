r1 = int(input("Enter r1: "))
c1 = int(input("Enter c1: "))
r2 = int(input("Enter r2: "))
c2 = int(input("Enter c2: "))

if c1 != r2:
    print("ERROR: Multiplication not possible.")
    exit()

A, B = [], []

print("Enter A:")
for i in range(r1):
    temp = []
    for j in range(c1):
        temp.append(int(input(f"Enter value {i}{j}: ")))
    A.append(temp)
print("Enter B:")
for i in range(r2):
    temp = []
    for j in range(c2):
        temp.append(int(input(f"Enter value {i}{j}: ")))
    B.append(temp)

C = []
for i in range(r1):
    temp = []
    for j in range(c2):
        val = 0
        for k in range(c1):
            val += A[i][k] * B[k][j]
        temp.append(val)
    C.append(temp)

T = []
for j in range(c1):
    temp = []
    for i in range(r1):
        temp.append(A[i][j])
    T.append(temp)

print("A:")
for i in A:
    print(i)

print("B:")
for i in B:
    print(i)

print("Multiplication Result C:")
for i in C:
    print(i)

print("Transpose of A:")
for i in T:
    print(i)

