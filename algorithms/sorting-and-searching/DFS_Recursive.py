graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}


def dfs_aux(input_graph, current_node, target_node):
    dfs(input_graph, current_node, target_node, [])


def dfs(input_graph, current_node, target_node, visited_nodes):
    visited_nodes.append(current_node)
    print("Visiting", current_node)
    # print("Visited", visited_nodes)
    if current_node == target_node:
        print("Found target", target_node)
        return True
    neighbours = input_graph.get(current_node)
    # print("Inspecting neighbours", neighbours)
    for (neighbour, weight) in neighbours:
        if neighbour not in visited_nodes:
            found = dfs(input_graph, neighbour, target_node, visited_nodes)
            if found:
                return True
    return False


dfs_aux(graph, 1, 6)
dfs_aux(graph, 1, 5)
