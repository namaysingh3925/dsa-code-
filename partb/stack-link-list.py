class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def push(self, d):
        n = self.Node(d)
        n.next = self.top
        self.top = n
        self.size += 1

    def pop(self):
        if self.top == None:
            print("Stack is Underflow")
            return None
        temp = self.top
        self.top = self.top.next
        self.size -= 1
        return temp.data

    def peek(self):
        if self.top == None:
            print("Stack is Underflow")
            return None
        return self.top.data

    def traversal(self):
        if self.top == None:
            print("Stack is Underflow")
        else:
            temp = self.top
            while temp.next != None:
                print(temp.data, end="->")
                temp = temp.next
            print(temp.data )

s = Stack()

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Traversal  5.Size  6.Exit")
    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            val = int(input("Enter value: "))
            s.push(val)
        case 2:
            x = s.pop()
            if x != None:
                print("Popped:", x)
        case 3:
            x = s.peek()
            if x != None:
                print("Top:", x)
        case 4:
            s.traversal()
        case 5:
            print("Size =", s.size)
        case 6:
            break
        case _:
            print("Invalid choice")
