class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, d):
        self.data.append(d)

    def dequeue(self):
        if len(self.data) == 0:
            print("Queue Underflow")
            return None
        return self.data.pop(0)
    def first(self):
        if len(self.data) == 0:
            print("Queue Underflow")
            return None
        return self.data[0]

    def traversal(self):
        if len(self.data) == 0:
            print("Queue is Empty")
        else:
            print(self.data)

q = Queue()
while True:

    print("\n1.Enqueue  2.Dequeue  3.First  4.Traversal  5.Exit")
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
            x = q.first()
            if x != None:
                print("Front:", x)

        case 4:
            q.traversal()

        case 5:
            break

        case _:
            print("Invalid choice")
