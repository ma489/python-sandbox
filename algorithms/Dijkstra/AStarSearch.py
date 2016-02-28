import sys

# A* search - used to find least-cost path through graph/tree

# #### initialisation

INFINITY = sys.maxsize

graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}

initial_node = 1
target_node = 5 # try different values here

h_score = {  # My guess at the 'straight-line' distances of this made-up graph (a heuristic) to the goal
    1: 10,
    2: 8,
    3: 7,
    4: 2,
    5: 0,
    6: 3
}

g_score = {
    initial_node: 0
}

for node in graph.keys():
    if node != initial_node:
        g_score.update({node: INFINITY})

f_score = {
    initial_node: h_score.get(initial_node)
}  # f = g + h
for node in graph.keys():
    if node != initial_node:
        f_score.update({node: INFINITY})

openSet = [initial_node]
closedSet = []
cameFrom = {}


# #### search

def get_next_best_node_from_open_set():  # priority queue would make this more efficient
    openSet.sort(key=lambda x: f_score.get(x))
    return openSet[0]


def reconstruct_path(from_node):
    path = [from_node]
    while from_node in cameFrom.keys():
        from_node = cameFrom.get(from_node)
        path = [from_node] + path
    print("Path:", path)

print("Source:", initial_node)
print("Target:", target_node)
print("Running")

while openSet:
    current_node = get_next_best_node_from_open_set()
    if current_node == target_node:
        print("Found", current_node)
        reconstruct_path(current_node)
        break
    openSet.remove(current_node)
    closedSet.append(current_node)
    for neighbour in graph.get(current_node):
        neighbour_id = neighbour[0]
        edge_weight = neighbour[1]
        if neighbour_id in closedSet:  # already visited this neighbour
            continue
        tentative_g_score = g_score.get(current_node) + edge_weight
        if neighbour_id not in openSet:  # not yet discovered, so no g_score yet
            openSet.append(neighbour_id)
        elif tentative_g_score >= g_score.get(neighbour_id):  # this route is not an improvement
            continue
        cameFrom.update({neighbour_id: current_node})
        g_score.update({neighbour_id: tentative_g_score})
        f_score.update({neighbour_id: tentative_g_score + h_score.get(neighbour_id)})

print("Done running.")
