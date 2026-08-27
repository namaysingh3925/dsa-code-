while True:
    print("\n--- Simple Calculator ---")
    print("1.   Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program terminated")
        break

    A = float(input("Enter first number: "))
    B = float(input("Enter second number: "))

    match choice:

        case 1:
            result = A + B
            print("Result =", result)

        case 2:
            result = A - B
            print("Result =", result)

        case 3:
            result = A * B
            print("Result =", result)

        case 4:
            if B != 0:
                result = A / B
                print("Result =", result)
            else:
                print("Division by zero not allowed")
        case _:
            print("Invalid choice")
