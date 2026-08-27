def push(stack, item):
    stack.append(item)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    return None

def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    return None

def is_empty(stack):
    return len(stack) == 0

def precedence(op):
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for char in expression:
        if char.isalnum():
            postfix += char

        elif char == '(':
            push(stack, char)

        elif char == ')':
            while not is_empty(stack) and peek(stack) != '(':
                postfix += pop(stack)
            pop(stack)

        else:
            while (not is_empty(stack) and
                   precedence(peek(stack)) >= precedence(char)):
                postfix += pop(stack)
            push(stack, char)

    while not is_empty(stack):
        postfix += pop(stack)

    return postfix


infix = input("Infix: ")
postfix = infix_to_postfix(infix)

print("Postfix:", postfix)
