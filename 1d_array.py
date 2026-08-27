n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

total = 0
minimum = arr[0]
maximum = arr[0]

for num in arr:
    total = total + num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

average = total / n

print("Sum =", total)
print("Average =", average)
print("Minimum =", minimum)
print("Maximum =", maximum)
 