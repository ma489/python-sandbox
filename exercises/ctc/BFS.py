# breadth-first search
from queue import Queue

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}

source_node = 1
target_node = 5


# TODO at some point make this bidirectional
def bfs(source, target):
    visited = []
    q = Queue()
    q.put(source)
    visited.append(source)
    while q.qsize() > 0:
        current_node = q.get()
        if current_node == target:
            print("Found target", current_node)
            break
        print("Visited", current_node)
        for neighbour in graph.get(current_node):
            neighbour_id = neighbour[0]
            if neighbour_id not in visited:
                visited.append(neighbour_id)
                q.put(neighbour_id)


print("Running: %d to %d ..." % (source_node, target_node))
bfs(source_node, target_node)
print("Done.")
