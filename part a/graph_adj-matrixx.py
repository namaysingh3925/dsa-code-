v = int(input("Enter the number of vertices: "))
A = []

for i in range(v):
    A.append([0] * v)
e = int(input("Enter the number of edges: "))
edges = []

for m in range(e):
    print("Enter", m + 1, "th edge")
    i = int(input("u: "))
    j = int(input("v: "))
    A[i - 1][j - 1] = 1
    A[j - 1][i - 1] = 1
    edges.append((i, j))

print("\nAdjacency Matrix:")
for i in range(v):
    print(A[i])

# -------- ADJACENCY LIST --------
class GraphList:
    head = None
    class NodeEdge:
        def __init__(self, data):
            self.edge = data
            self.next = None

    class NodeVertix:
        def __init__(self, data):
            self.data = data
            self.next_vertex = None
            self.edge_list = None

    def insert_vertex(self, x):
        new = self.NodeVertix(x)
        if self.head == None:
            self.head = new
        else:
            temp = self.head
            while temp.next_vertex != None:
                temp = temp.next_vertex
            temp.next_vertex = new
   

    def insert_edge(self, u, v):
        t = self.head
        while t != None and t.data != u:
            t = t.next_vertex
        if t == None:
            print("Vertex not found")
            return
        r = t.edge_list
        n = self.NodeEdge(v)
        if r == None:
            t.edge_list = n
        else:
            while r.next != None:
                r = r.next
            r.next = n

    def traverse(self):
        if self.head == None:
            print("Graph Empty")
        else:
            d = self.head
            while d != None:
                print(d.data, end="->")
                b = d.edge_list
                while b != None:
                    print(b.edge, end="->")
                    b = b.next
                print(None)
                d = d.next_vertex

# -------- GRAPH CREATION --------
g = GraphList()
for i in range(1, v + 1):
    g.insert_vertex(i)
for u, v in edges:
    g.insert_edge(u, v)
    g.insert_edge(v, u)
print("\nAdjacency List:")
g.traverse()
