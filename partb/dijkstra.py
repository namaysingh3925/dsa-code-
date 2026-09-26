class Graph:

    def __init__(self, v):
        self.v = v
        self.g = {}
        for i in range(v):
            self.g[i] = []

    def add_edge(self, u, v, directed=False):
        if directed:
            self.g[u].append(v)
        else:
            self.g[u].append(v)
            self.g[v].append(u)

    def dfs_undirected(self, start, visited, parent):
        visited[start] = True
        print(start, end=" ")
        for adj in sorted(self.g[start]):
            if visited[adj] == False:
                if self.dfs_undirected(adj, visited, start):
                    return True
            elif adj != parent:
                return True
        return False

    def dfs_directed(self, start, visited, rec):
        visited[start] = True
        rec[start] = True
        print(start, end=" ")
        for adj in sorted(self.g[start]):
            if visited[adj] == False:
                if self.dfs_directed(adj, visited, rec):
                    return True
            elif rec[adj] == True:
                return True
        rec[start] = False
        return False

v = int(input("Enter number of vertices: "))
df = Graph(v)
d = input("Enter d for directed graph and u for undirected graph: ")
e = int(input("Enter number of edges: "))

for i in range(e):
    print("Enter the", i + 1, "th edge")
    uu = int(input("Enter u: "))
    vv = int(input("Enter v: "))
    if d == "d":
        df.add_edge(uu, vv, True)
    else:
        df.add_edge(uu, vv)


visited = {}
for i in range(v):
    visited[i] = False

start = int(input("Enter the start vertex: "))
print("DFS Traversal:")

if d == "d":
    rec = {}
    for i in range(v):
        rec[i] = False
    e = df.dfs_directed(start, visited, rec)
else:
    e = df.dfs_undirected(start, visited, -1)
print()

if e:
    print("Cycle Present")

else:
    print("Cycle Not Present")


