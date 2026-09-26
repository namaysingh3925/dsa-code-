class Graph:
    def __init__(self, v):
        self.v = v
        self.g = {}

        for i in range(v):
            self.g[i] = []

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=" ")
        for adj in sorted(self.g[start]):
            if visited[adj] == False:
                self.dfs(adj, visited)

v = int(input("Enter number of vertices: "))
df = Graph(v)
e = int(input("Enter number of edges: "))

for i in range(e):
    print("Enter the", i + 1, "th edge")
    uu = int(input("Enter u: "))
    vv = int(input("Enter v: "))
    df.add_edge(uu, vv)

visited = {}

for i in range(v):
    visited[i] = False

start = int(input("Enter the start vertex: "))
print("DFS Traversal:")
df.dfs(start, visited)
print()
