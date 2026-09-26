class CQ:
    MAX_CAPACITY = 10

    def __init__(self):
        self.cq = [None] * self.MAX_CAPACITY
        self.f = -1
        self.r = -1
        self.size = 0

    def enqueue(self, x):
        if (self.r + 1) % self.MAX_CAPACITY == self.f:
            print("Queue Overflow")
        elif self.size == 0:
            self.f = self.r = 0
            self.cq[self.r] = x
            self.size += 1
        else:
            self.r = (self.r + 1) % self.MAX_CAPACITY
            self.cq[self.r] = x
            self.size += 1



    def dequeue(self):
        if self.size == 0:
            print("Queue Underflow")
            return None
        x = self.cq[self.f]
        self.cq[self.f] = None
        self.f = (self.f + 1) % self.MAX_CAPACITY
        self.size -= 1
        if self.size == 0:
            self.f = self.r = -1
        return x

    def first(self):
        if self.size == 0:
            print("Queue Underflow")
            return None
        return self.cq[self.f]

    def display(self):
        print(self.cq)

q = CQ()

while True:
    print("\n1.Enqueue  2.Dequeue  3.First  4.Display  5.Exit")
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
            q.display()

        case 5:
            break

        case _:
            print("Invalid choice")

