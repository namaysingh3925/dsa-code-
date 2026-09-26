queue = []

def enqueue(x):
    queue.append(x)

def dequeue():
    return queue.pop(0)

def is_empty():
    if len(queue) == 0:
        return True
    else:
        return False

graph = {

    "A": ["B", "D", "C"],
    "B": ["A", "E"],
    "C": ["D", "A", "F"],
    "D": ["A", "G", "E", "C"],
    "E": ["D", "G", "B"],
    "F": ["C", "G"],
    "G": ["D", "F", "E"]
}

def bfs(start):
    visited = []
    visited.append(start)
    enqueue(start)
    print("BFS Traversal:")
    while queue:
        v = dequeue()
        print(v, end=" ")
        for n in sorted(graph[v]):
            if n not in visited:
                visited.append(n)
                enqueue(n)
    print()

start = input("Enter starting vertex: ")
bfs(start)
