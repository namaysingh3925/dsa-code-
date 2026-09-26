def is_matched(expr):
    lefty = "({["
    righty = ")}]"
    stack = []

    for c in expr:
        if c in lefty:
            stack.append(c)

        elif c in righty:
            if len(stack) == 0:
                return False

            if righty.index(c) != lefty.index(stack.pop()):
                return False

    return len(stack) == 0


expr = input("Enter expression: ")

if is_matched(expr):
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")
