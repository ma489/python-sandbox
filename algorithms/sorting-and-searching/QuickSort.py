# quicksort - both inplace and non-inplace


import random


def quicksort(input_list):
    # print("Input List", input_list)
    if len(input_list) == 0:
        return []
    if len(input_list) == 1:
        return input_list
    pivot_position = random.randint(0, len(input_list) - 1)
    pivot_value = input_list[pivot_position]
    # print("Pivot position:", pivot_position,"Pivot value:", pivot_value)
    lesser_partition = [x for x in input_list if x < pivot_value]
    # print("Lesser partition", lesser_partition)
    greater_partition = [x for x in input_list if x > pivot_value]
    # print("Greater partition", greater_partition)
    return quicksort(lesser_partition) + [pivot_value] + quicksort(greater_partition)


def quicksort_inplace(input_list):
    qs_inplace(input_list, 0, len(input_list)-1)


def qs_inplace(input_list, partition_start, partition_end):
    # print("Partition start", partition_start, "Partition end", partition_end)
    if partition_end <= partition_start:
        return
    pivot_position = partition_end
    pivot_value = input_list[pivot_position]
    # print("Pivot position:", pivot_position, "Pivot value:", pivot_value)
    new_partition_point = partition(input_list, partition_start, partition_end, pivot_position, pivot_value)
    # print("Intermediate list", input_list)
    qs_inplace(input_list, partition_start, new_partition_point-1) # recurse on lower partition
    qs_inplace(input_list, new_partition_point+1, partition_end) # recurse on upper partition


# create_partitions_around_pivot_value_and_get_new_partition_point
def partition(input_list, partition_start, partition_end, pivot_position, pivot_value):
    swap_space_position = partition_start
    for i in range(partition_start, partition_end): # excludes end point, I think TODO check
        if input_list[i] <= pivot_value:
            swap(input_list, i, swap_space_position)
            swap_space_position += 1
    swap(input_list, pivot_position, swap_space_position)
    return swap_space_position


def swap(input_list, a, b):
    temp = input_list[b]
    input_list[b] = input_list[a]
    input_list[a] = temp


print("Standard")
my_list = [8, 3, 0, 1, 5, 9, 2, 7, 4, 6]
print(my_list)
result = quicksort(my_list)
print(result)

print("In-place")
my_list = [8, 3, 0, 1, 5, 9, 2, 7, 4, 6]
print(my_list)
quicksort_inplace(my_list)
print(my_list)