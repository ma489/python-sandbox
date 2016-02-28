import time

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}


def dfs(input_graph, start_node):
    visited_nodes = []
    to_be_visited_stack = [start_node]
    while to_be_visited_stack:
        print("to_be_visited_stack", to_be_visited_stack)
        print("visited_nodes", visited_nodes)
        current_node = to_be_visited_stack.pop()
        if current_node in visited_nodes:
            continue
        print("Visiting", current_node)
        visited_nodes.append(current_node)
        for (neighbour, weight) in input_graph.get(current_node):
            to_be_visited_stack.append(neighbour)


def dfs_search(input_graph, start_node, target_node):
    visited_nodes = []
    to_be_visited_stack = [start_node]
    while to_be_visited_stack:
        print("to_be_visited_stack", to_be_visited_stack)
        print("visited_nodes", visited_nodes)
        current_node = to_be_visited_stack.pop()
        if current_node == target_node:
            print("Found target", target_node)
            return
        if current_node in visited_nodes:
            continue
        print("Visiting", current_node)
        visited_nodes.append(current_node)
        for (neighbour, weight) in input_graph.get(current_node):
            to_be_visited_stack.append(neighbour)


print("Search")
dfs_search(graph, 1, 6)
print("Non-Search")
dfs(graph, 1)
