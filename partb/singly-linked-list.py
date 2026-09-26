class SLL:
    def __init__(self):
        self.head = None
        self.size = 0

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def insertAtBeginning(self, d):
        n = self.Node(d)
        n.next = self.head
        self.head = n
        self.size += 1

    def removeAtBeginning(self):
        if self.head == None:
            print("LL is Underflow")
            return None
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp.data

    def insertAtLast(self, d):
        n = self.Node(d)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n
        self.size += 1

    def removeAtLast(self):
        if self.head == None:
            print("LL is underflow")
            return None
        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.size -= 1
            return temp.data
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            y = temp.next
            temp.next = None
            self.size -= 1
            return y.data

    def traversal(self):
        if self.head == None:
            print("LL is Underflow")
        else:
            temp = self.head
            while temp.next != None:
                print(temp.data, end="->")
                temp = temp.next
            print(temp.data)

l = SLL()

while True:

    print("\n1.Insert Beginning  2.Insert End  3.Delete Beginning  4.Delete End  5.Traversal  6.Size  7.Exit")

    ch = int(input("Enter choice: "))

    match ch:
        case 1:
            val = int(input("Enter value: "))
            l.insertAtBeginning(val)
        case 2:
            val = int(input("Enter value: "))
            l.insertAtLast(val)
        case 3:
            x = l.removeAtBeginning()
            if x != None:
                print("Deleted:", x)
        case 4:
            x = l.removeAtLast()
            if x != None:
                print("Deleted:", x)
        case 5:
            l.traversal()
        case 7:
            break
        case _:
            print("Invalid choice")
