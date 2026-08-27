stack = []

def push(e):
    stack.append(e)

def is_empty():
    return len(stack) == 0

def pop():
    if is_empty():
        print("Stack Underflow")
        return None
    return stack.pop()

p = input("Enter postfix expression: ")
for i in p:
    if i.isdigit():
        push(int(i))
    else:
        op2 = pop()
        op1 = pop()

        if i == "+":
            push(op1 + op2)

        elif i == "-":
            push(op1 - op2)

        elif i == "*":
            push(op1 * op2)

        elif i == "/":
            push(op1 / op2)

        else:
            print("Invalid operator")
print("Result:", pop())
