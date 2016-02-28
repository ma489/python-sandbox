# Prim's algorithm for minimum spanning tree of graph

# Steps:
# 1 - Initialise tree with randomly selected vertex
# 2 - Grow the tree by one edge (criteria: minimum weight, and one of the vertices is not already in the tree)
# 3 - Repeat step 2 until all vertices are in tree

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}


def prim(input_graph):
    vertices_in_tree = []
    vertices_not_in_tree = list(graph.keys())
    tree = []
    initial_vertex = vertices_not_in_tree[0]
    vertices_in_tree.append(initial_vertex)
    vertices_not_in_tree.remove(initial_vertex)
    while vertices_not_in_tree:  # i.e. while its not empty
        # print("Loop")
        # print("Tree", tree)
        candidate_edges = []
        for v in vertices_in_tree:
            edges_from_v = graph.get(v)
            augmented_edges = list(map(lambda x: (v, x[0], x[1]), edges_from_v))
            filtered_augmented_edges = [x for x in augmented_edges if x[1] not in vertices_in_tree]
            candidate_edges.extend(filtered_augmented_edges)
        candidate_edges.sort(key=lambda x: x[2])
        # print("Candidates", candidate_edges)
        candidate = candidate_edges[0]
        # print("Candidate", candidate)
        vertices_in_tree.append(candidate[1])
        # print("Removing", candidate[1], vertices_not_in_tree)
        vertices_not_in_tree.remove(candidate[1])
        tree.append(candidate)
    return tree


print("Running Prim's")
mst = prim(graph)
print("MST: ", mst)
