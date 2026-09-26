class QSLL:

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def __init__(self):

        self.f = None
        self.r = None
    def enqueue(self, d):
        n = self.Node(d)
        if self.r == None:
            self.r = self.f = n
        else:
            self.r.next = n
            self.r = n

    def dequeue(self):
        if self.f == None:
            print("Queue Underflow")
            return None
        temp = self.f
        self.f = self.f.next
        if self.f == None:
            self.r = None
        return temp.data

    def front(self):
        if self.f == None:
            print("Queue Underflow")
            return None
        return self.f.data

    def traversal(self):
        if self.f == None:
            print("Queue Underflow")
        else:
            temp = self.f
            while temp.next != None:
                print(temp.data, end="->")
                temp = temp.next
            print(temp.data)

q = QSLL()

while True:

    print("\n1.Enqueue  2.Dequeue  3.Front  4.Traversal  5.Exit")

    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            val = int(input("Enter value: "))
            q.enqueue(val)
        case 2:
            x = q.dequeue()
            if x != None:
                print("Deleted:", x)

        case 3:
            x = q.front()

            if x != None:
                print("Front:", x)

        case 4:
            q.traversal()

        case 5:
            break

        case _:
            print("Invalid choice")
