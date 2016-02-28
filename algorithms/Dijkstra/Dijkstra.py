# imports
from queue import PriorityQueue
import sys

# ### initialisation


class DistancePair(object):
    def __init__(self, node, distance):
        self.distance = distance
        self.node = node

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __hash__(self, *args, **kwargs):
        return super().__hash__(*args, **kwargs)


# graph represented as adjacency list with weights (neighbour_node, weight)
INFINITY = sys.maxsize
graph = {
    1: [(2, 7), (3, 9), (6, 14)],
    2: [(1, 7), (3, 10), (4, 15)],
    3: [(1, 9), (2, 10), (4, 11), (6, 2)],
    4: [(2, 15), (3, 11), (5, 6)],
    5: [(4, 6), (6, 9)],
    6: [(1, 14), (3, 2), (5, 9)]
}

# source node from which distances should be calculated
initial_node = 1 # 'source'

# setup tentative distances
tentative_distances = {initial_node: 0} # provides random access lookup of node distances, needed when comparing routes

unvisited_nodes = []
vertex_set_priority_queue = PriorityQueue() # needed to get next 'best' node, but provides no random access lookup
vertex_set_priority_queue.put(DistancePair(initial_node, 0))
unvisited_nodes.append(initial_node) # needed for random access lookup of whether node has been visited or not
for node in graph.keys():
    if node != initial_node:
        tentative_distances.update({node: INFINITY})
        vertex_set_priority_queue.put(DistancePair(node, INFINITY)) # add to priority queue
        unvisited_nodes.append(node)

# #### actual search algorithm:


while vertex_set_priority_queue.qsize() > 0: #while priority Q is not empty # |V| iterations
    # extract-min (log v)
    current_node = vertex_set_priority_queue.get() # get 'best' node - next closes to source
    neighbours = graph.get(current_node.node)
    if not neighbours:
        continue
    for neighbour in neighbours: # |E| iterations
        neighbour_node_id = neighbour[0]
        if neighbour_node_id in unvisited_nodes:
            edge_weight = neighbour[1]
            distance_to_current_node = tentative_distances.get(current_node.node)
            new_distance = distance_to_current_node + edge_weight
            old_distance_to_this_neighbour = tentative_distances.get(neighbour_node_id)
            if new_distance < old_distance_to_this_neighbour:
                tentative_distances.update({neighbour_node_id: new_distance})
                # decrease priority (log v)
                vertex_set_priority_queue.queue.remove(DistancePair(neighbour_node_id, old_distance_to_this_neighbour))
                vertex_set_priority_queue.put(DistancePair(neighbour_node_id, new_distance))
    unvisited_nodes.remove(current_node.node)

# print distances
print(tentative_distances)
