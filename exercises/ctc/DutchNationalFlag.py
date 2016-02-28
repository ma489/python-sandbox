# Dutch National Flag problem (quicksort partitioning)
import operator


def dnf(array, index):
    pivot_value = array[index]
    print("Pivot value", pivot_value)
    create_less_than_partition(array, index, pivot_value, operator.lt, 0)
    print(array)
    create_greater_than_partition(array, index, pivot_value, operator.gt, len(array)-1)
    # create_less_than_partition(array, index, pivot_value, operator.eq)


def create_less_than_partition(array, index, pivot_value, relation, swap_space):
    for j in range(1, len(array)):
        print("j", j)
        if j == index:
            swap_space += 1
            continue
        if relation(array[j], pivot_value):
            print("moving %d to %d" % (array[j], swap_space))
            temp = array[swap_space]
            array[swap_space] = array[j]
            array[j] = temp
        swap_space += 1


def create_greater_than_partition(array, index_, pivot_value, relation, swap_space):
    for j in range(len(array)-1, -1, -1):
        print("j", j)
        print("swap_space", swap_space)
        if j == index_:
            # swap_space -= 1
            continue
        if relation(array[j], pivot_value):
            print("moving %d to %d" % (array[j], swap_space))
            temp = array[swap_space]
            array[swap_space] = array[j]
            array[j] = temp
        swap_space -= 1


input_array = [3,1,4,5,2]
index = 2 # pivot 2; expecting: [1,4,3,2,5]

print("Input", input_array)
print("Index", index)
dnf(input_array, index)
print("Output", input_array)
