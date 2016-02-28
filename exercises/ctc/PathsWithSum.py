from ctc.Node import Node

# Paths with sum problem

# tree
nodeMinus4 = Node(-4, None, None)
nodeMinus1 = Node(-1, None, None)
nodeMinus2 = Node(-2, nodeMinus4, nodeMinus1)
node7 = Node(7, None, None)
node5 = Node(5, nodeMinus2, node7)
node22 = Node(22, None, None)
node13 = Node(13, None, None)
node20 = Node(20, node13, node22)
node10 = Node(10, node5, node20)
root = node10
nodes = [node10, node20, node13, node22, node7, nodeMinus1, nodeMinus4, nodeMinus2, node5]

count = 0
desired_sum = 13
paths = []
pathCost = {}

i = 0


def fun(sum_so_far, node, path):
    global i
    i += 1
    # print(node)
    sum_at_node = sum_so_far + node.id
    if sum_at_node == desired_sum:
        if path not in paths:
            paths.append(path)
            print("Found path!")
            print_path(path)
            global count
            count += 1
            pathCost.update({tuple(path): sum_at_node})
        else:
            print("Duplicate path! ")
            print_path(path)
    if node.left is not None:
        # print("trying left with parent")
        left_ = path + [node.left]
        if pathCost.get(tuple(left_)) is not None:
            print("Already calculated this path")
        if left_ not in paths:
            fun(sum_at_node, node.left, left_)
            # print("trying left")
            # fun(0, node.left, [node.left])
    if node.right is not None:
        # print("trying right with parent")
        right_ = path + [node.right]
        if right_ not in paths:
            fun(sum_at_node, node.right, right_)
            # print("trying right")
            # fun(0, node.right, [node.right])


def preorder(node, path, prepaths):
    # print_path(path)
    paths.append(path)
    prepaths.append(path)
    if node.left is not None:
        preorder(node.left, path + [node.left], prepaths)
    if node.right is not None:
        preorder(node.right, path + [node.right], prepaths)


def print_path(path):
    path_string = ""
    for p in path:
        path_string += str(p.id) + ", "
    m = map(lambda x: str(x.id), path)
    print(", ".join(m))


# print("Running...")
# fun(0, root, [root])
# for nod in nodes:
#     fun(0, nod, [nod])
# print("...Done!")
# print(i)
# print("Number of paths", count)
# for pat in paths:
#     print("path:")
#     print_path(pat)

prepaths = []
preorder(root, [root], prepaths)
for pt in prepaths:
    print_path(pt)
#TODO run Kadane's on prepaths
# this is an O(N) solution