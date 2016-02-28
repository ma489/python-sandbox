# Longest Increasing Subsequence


def lis(input_):
    memo = {}
    memo.update({0: input_[0]})
    for i in range(0, len(input_)):
        value = []
        for j in range(0, i):
            # print(i)
            # print(j, i)
            if j >= i:
                continue
            print("j:", j, ", input value at j:", input_[j])
            if input_[j] < input_[i]:
                # print(i, input_[i], j, input_[j])
                tentative = memo.get(j)
                if len(tentative) > len(value):
                    value = tentative
        value.append(input_[i])
        print("i:", i, ", input value at i:", input_[i], ", memo_value at i:", value)
        memo.update({i: value})
    return memo


input_sequence = [3, 2, 6, 4, 5, 1]
print("Input", input_sequence)
result = lis(input_sequence)
print("Result", result)
