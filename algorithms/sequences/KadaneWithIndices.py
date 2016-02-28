
def max_sub_array(input_array):
    max_so_far = 0
    max_to_this_point = 0
    start = 0
    end = 0
    best_start = 0
    best_end = 0
    i = 0 #to avoid duplicates
    for x in input_array:
        end = i
        print("x", x)
        print("start", start)
        print("end", end)
        print("---")
        tentative_max = x + max_to_this_point
        if tentative_max > 0: # lets not go negative
            max_to_this_point = tentative_max # update end
            # end = input_array.index(x)
        else:
            max_to_this_point = 0
            start = i + 1
            # end = start
        if tentative_max > max_so_far:
            max_so_far = tentative_max
            best_start = start
            best_end = end
        i += 1
    return max_so_far, best_start, best_end


my_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("my_array", my_array)
(max_sum, start_index, end_index) = max_sub_array(my_array)
print("max_sum", max_sum)
print("start", start_index)
print("end", end_index)
