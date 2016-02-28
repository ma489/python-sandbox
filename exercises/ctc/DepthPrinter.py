from ctc.Node import Node

# tree
node2 = Node(2, None, None)
node1 = Node(1, None, None)
node4 = Node(4, node2, node1)
node6 = Node(6, None, None)
node20 = Node(20, None, None)
node10 = Node(10, node6, node20)
node8 = Node(8, node4, node10)
root = node8


def fun(node, depth, lists):
    if lists.get(depth) is None:
        lists.update({depth: []})
    nodes_at_this_depth = lists.get(depth)
    nodes_at_this_depth.append(node)
    if node.left is not None:
        fun(node.left, depth+1, lists)
    if node.right is not None:
        fun(node.right, depth+1, lists)


result = {}
print(result)
fun(node8, 1, result)
for key in result.keys():
    print("Level: ", key)
    for nod in result.get(key):
        print(" ", nod)
