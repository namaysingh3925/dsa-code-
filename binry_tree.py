class BT:

    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, d, p=None, l=None, r=None):
            self.data = d
            self.parent = p
            self.left = l
            self.right = r

    def create_node(self, d, p=None, l=None, r=None):
        n = self.Node(d, p, l, r)
        return n

    def assign_root(self, n):
        if self.root != None:
            print("Root is already present")
            return None
        self.root = n

    def assign_left(self, parent, left):
        if parent.left != None:
            print("Left exists")
        else:
            parent.left = left
            left.parent = parent

    def assign_right(self, parent, right):
        if parent.right != None:
            print("Right exists")
        else:
            parent.right = right
            right.parent = parent

    def preorder(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")


# -------- TREE CREATION --------
bt = BT()

n = bt.create_node(12)
bt.assign_root(n)

n1 = bt.create_node(13)
n2 = bt.create_node(14)

bt.assign_left(n, n1)
bt.assign_right(n, n2)

n3 = bt.create_node(15)
n4 = bt.create_node(16)

bt.assign_left(n1, n3)
bt.assign_right(n1, n4)


# -------- MENU --------
while True:
    print("\n1.Preorder  2.Inorder  3.Postorder  4.Exit")

    ch = int(input("Enter choice: "))

    match ch:

        case 1:
            print("Preorder Traversal:")
            bt.preorder(bt.root)
            print()
        case 2:
            print("Inorder Traversal:")
            bt.inorder(bt.root)
            print()

        case 3:
            print("Postorder Traversal:")
            bt.postorder(bt.root)
            print()

        case 4:
            break

        case _:
            print("Invalid choice")
