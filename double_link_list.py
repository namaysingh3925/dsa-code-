class DLL:

    def __init__(self):
        self.head = None
    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None
            self.prev = None

    def insertAtBeginning(self, x):
        n = self.Node(x)
        if self.head != None:
            self.head.prev = n
            n.next = self.head
        self.head = n

    def traversal(self):
        if self.head is None:
            print("DLL Underflow")
        else:
            temp = self.head
            while temp.next is not None:
                print(temp.data, end="<->")
                temp = temp.next
            print(temp.data)

    def removeAtLast(self):
        if self.head == None:
            print("DLL Underflow")
        elif self.head.next == None:
            val = self.head
            self.head = None
            print(val.data, "deleted")
        else:
            p = self.head
            while p.next != None:
                p = p.next
            val = p
            p.prev.next = None
            val.prev = None
            print(val.data, "deleted")

    def removeAtBeg(self):
        if self.head is None:
            print("DLL Underflow")
        else:
            data = self.head
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            print(data.data)

    def insertAtLast(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = new_node
            new_node.prev = p

d = DLL()

while True:
    print("\n1.Insert Beginning  2.Insert End  3.Delete Beginning")
    print("4.Delete End  5.Traversal  6.Exit")

    ch = int(input("Enter choice: "))

    match ch:

        case 1:
            val = int(input("Enter value: "))
            d.insertAtBeginning(val)

        case 2:
            val = int(input("Enter value: "))
            d.insertAtLast(val)

        case 3:
            d.removeAtBeg()

        case 4:
            d.removeAtLast()

        case 5:
            d.traversal()

        case 6:
            break

        case _:
            print("Invalid choice")
