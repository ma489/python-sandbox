# Add without plus


def add_without_plus(a, b):
    a_binary = [1, 1, 1, 0]
    b_binary = [0, 1, 0, 1]
    carry = [0, 0, 0, 0]
    pair_result = [0, 0, 0, 0]
    output_binary = [0, 0, 0, 0, 0]
    i = len(a_binary)
    z = zip(reversed(a_binary), reversed(b_binary))
    for (b1, b2) in z:
        print((b1, b2))
        pr = b1 ^ b2
        if pr == 1:
            output_binary[i] = 1
        pair_result[i] = pr
        car = carry[i]
        if pr == 1 and car == 1:
            car[i+1] = 1
        output_binary[i] = pair_result[i] ^ car
        i -= 1
    return 0


def get_binary_array(x):
    bin_array = []
    return []


a = 14
b = 5
print("A:", a)
print("B:", b)
result = add_without_plus(a, b)
print("Max:", result)
