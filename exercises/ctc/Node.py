class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

    def __str__(self):
        return "Node %d" % self.id