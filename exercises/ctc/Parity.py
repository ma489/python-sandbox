results = {}

def parity(x):
    print("X:", x)
    if x == 0: # special case
        # print("Iterations:", 0)
        return 0
    if (x & (x-1)) == 0: # powers of two
        # print("Iterations:", 0)
        return 1
    # print("Binary representation", bin(x))
    count_of_ones = 0
    mask = 1
    iterations = 0
    # print("Mask", bin(mask))
    while x > 0:
        iterations += 1
        # print(bin(x))
        masked_value = (x & mask)
        sub_problem_solution = results.get(masked_value)
        if sub_problem_solution is not None:
            # print("Already solved subproblem")
            count_of_ones += sub_problem_solution
            break
        if masked_value == 1:
            count_of_ones += 1
        x >>= 1
    # print("Count of ones", count_of_ones)
    # print("Iterations:", iterations)
    results.update({x: count_of_ones})
    if (count_of_ones & 1) == 1: # more efficient than mod
        return 1 # odd parity
    else:
        return 0 # even parity

for i in range(0,100):
    print("Parity:", parity(i))
# print(parity(5))
# print(parity(0))
# print(parity(1))
# print(parity(2))
# print(parity(3))
# print(parity(16))
# print(parity(17))
# print(parity(18))
# print(parity(19))
