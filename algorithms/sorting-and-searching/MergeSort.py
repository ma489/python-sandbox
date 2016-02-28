# Merge sort


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    halfway_point = int(len(input_list) / 2)
    # print("----input_list", input_list)
    # print("halfway_point", halfway_point)
    lower_sub_problem = input_list[0:halfway_point]
    upper_sub_problem = input_list[halfway_point:]
    solution_to_lower_sub_problem = merge_sort(lower_sub_problem)
    solution_to_upper_sub_problem = merge_sort(upper_sub_problem)
    # print("Merging", solution_to_lower_sub_problem, solution_to_upper_sub_problem)
    return merge(solution_to_lower_sub_problem, solution_to_upper_sub_problem)


def merge(list_a, list_b):
    merged_list = []
    value_a = list_a[0]
    value_b = list_b[0]
    # print("value_a", value_a, "value_b", value_b)
    while value_a is not None and value_b is not None:
        if value_a < value_b:
            merged_list.append(value_a)
            list_a.pop(0)
            value_a = maybe_get_value(list_a)
        elif value_b < value_a:
            merged_list.append(value_b)
            list_b.pop(0)
            value_b = maybe_get_value(list_b)
        else:
            merged_list.append(value_a)
            merged_list.append(value_b)
            list_a.pop(0)
            list_b.pop(0)
            value_a = maybe_get_value(list_a)
            value_b = maybe_get_value(list_b)
    # print("list_a", list_a, "list_b", list_b)
    merged_list.extend(list_a)
    merged_list.extend(list_b)
    # print("Merged", merged_list)
    return merged_list


def maybe_get_value(in_list):
    if in_list:
        return in_list[0]
    else:
        return None


print("Standard")
my_list = [8, 3, 0, 1, 5, 9, 2, 7, 4, 6]
print("Input", my_list)
result = merge_sort(my_list)
print("Output", result)

print("Odd number of elements")
my_list = [8, 3, 0, 1, 5, 9, 2, 7, 4, 6, 10]
print("Input", my_list)
result = merge_sort(my_list)
print("Output", result)

print("Duplicate 7")
my_list = [8, 3, 0, 1, 5, 9, 2, 7, 4, 7]
print("Input", my_list)
result = merge_sort(my_list)
print("Output", result)
