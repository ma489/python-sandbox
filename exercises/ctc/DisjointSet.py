class DisjointSet:
    def __init__(self):
        self.sets = []
        self.set_pointers = {}

    def make_set(self, x):
        new_set = [x]
        self.sets.append(new_set)
        self.set_pointers.update({x: self.sets.index(new_set)})
        return new_set

    def find_set(self, x):
        return self.set_pointers.get(x)

    def union(self, x, y):
        #print(self.sets)
        #print(self.set_pointers)
        #print("Unioning", x, y)
        set_id_of_x = self.find_set(x)
        set_id_of_y = self.find_set(y)
        #print("Corresponding sets", set_id_of_x, set_id_of_y)
        x_set = self.sets[set_id_of_x]
        y_set = self.sets[set_id_of_y]
        if len(x_set) > len(y_set):
            new_unioned_set = x_set + y_set
        else:
            new_unioned_set = y_set + x_set
        self.sets.append(new_unioned_set)
        self.sets.remove(x_set)
        self.sets.remove(y_set)
        new_index = self.sets.index(new_unioned_set)
        for e in new_unioned_set:
            # print(new_unioned_set)
            self.set_pointers.update({e: new_index})
        for (k,v) in self.set_pointers.items():
            if k not in new_unioned_set:
                if v > set_id_of_x:
                    self.set_pointers.update({k : v-1})
                if v > set_id_of_y:
                    self.set_pointers.update({k : v-2})
        #print("huh")


def make_disjoint_set(n):
    disjoint_set = DisjointSet()
    for x in range(1, 2 * n + 1):
        disjoint_set.make_set(x)
    return disjoint_set


def find_largest_connected_component(sets):
    max_size = 0
    for set_ in sets:
        set_size = len(set_)
        if (set_size > max_size) and (set_size > 1):
            max_size = set_size
    return max_size


def find_smallest_connected_component(sets):
    min_size = 100000000000
    for set_ in sets:
        set_size = len(set_)
        if (set_size < min_size) and (set_size > 1):
            min_size = set_size
    return min_size


def format_input(param):
    edges_list = list(map((lambda x: int(x)), param.split(" ")))
    return tuple(edges_list)


N = int(input())
#print(N)

edges = [format_input(input()) for _ in range(0, N)]
#print(edges)
#N = 5
disjointSet = make_disjoint_set(N)
#print(disjointSet.sets)
#print(disjointSet.set_pointers)

#edges = [(1, 6), (2, 7), (3, 8), (4, 9), (2, 6)]

for (v1, v2) in edges:
    if disjointSet.find_set(v1) != disjointSet.find_set(v2):
        disjointSet.union(v1, v2)
    #else:
        #print("%d and %d are in same set" % (v1, v2))
        #print(disjointSet.sets)
        #print(disjointSet.set_pointers)

# print(disjointSet.sets)

max_comp = find_largest_connected_component(disjointSet.sets)
# print("Max:", max_comp)
min_comp = find_smallest_connected_component(disjointSet.sets)
# print("Min", min_comp)
print(min_comp, max_comp)
