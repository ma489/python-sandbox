# BFS
from collections import deque

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}

def bfs_search(input_graph, start_node, target_node):
    visited_nodes = []
    to_be_visited_queue = deque([start_node])
    while to_be_visited_queue:
        current_node = to_be_visited_queue.popleft() # get item from start of queue
        print("Visiting", current_node)
        if current_node == target_node:
            print("Found target", current_node)
            return
        if current_node in visited_nodes:
            continue
        visited_nodes.append(current_node)
        for (neighbour, weight) in input_graph.get(current_node):
            if neighbour not in visited_nodes and neighbour not in to_be_visited_queue:
                to_be_visited_queue.append(neighbour)
        # print(to_be_visited_queue)

def bfs(input_graph, start_node):
    visited_nodes = []
    to_be_visited_queue = deque([start_node])
    while to_be_visited_queue:
        current_node = to_be_visited_queue.popleft() # get item from start of queue
        print("Visiting", current_node)
        if current_node in visited_nodes:
            continue
        visited_nodes.append(current_node)
        for (neighbour, weight) in input_graph.get(current_node):
            if neighbour not in visited_nodes and neighbour not in to_be_visited_queue:
                to_be_visited_queue.append(neighbour)
        # print(to_be_visited_queue)


print("Non-search")
bfs(graph, 1)
print("Search")
bfs_search(graph, 1, 5)