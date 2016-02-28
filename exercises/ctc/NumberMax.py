def number_max(a, b):
    #result_map = {0: a, 1: b}
    bits = 32
    mask = 1 << bits
    print("Mask", bin(mask))
    a_minus_b = (a - b) #TODO consider underflow/overflow?
    print("A-B:", bin(a_minus_b), a_minus_b)
    k = a_minus_b & mask
    print("Intermediate:", bin(k))
    k >>= bits
    print("K:", k)
    # k = 1 if A > B, 0 otherwise
    #return result_map.get(k)
    return a*(not k) + b*(k)


a = 24
b = 5500000000000000000000000#0
print("A:", a)
print("B:", b)
max_num = number_max(a, b)
print("Max:", max_num)
