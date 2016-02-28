import random


def shuffle(list):
    if list is None:
        return []
    n = len(list)
    # print("n", n)
    if n <= 1:
        return list
    else:
        item = list[random.randint(0, n - 1)]
        # print("item", item)
        # print("list", list)
        list.remove(item)
        # print("remaining", list)
        return [item] + shuffle(list)


my_list = [1, 2, 3, 4, 5, 6]
print("my_list", my_list)
print("Shuffling...")
shuffled_list = shuffle(my_list)
print("my_list", shuffled_list)

results = {}

for i in range(0,1000):
    my_list = [1, 2, 3, 4, 5, 6]
    shuffled_list = shuffle(my_list)
    list_key = tuple(shuffled_list)
    count = results.get(list_key)
    if count is None:
        count = 1
    else:
        count += 1
    results.update({list_key: count})

print(results.values())