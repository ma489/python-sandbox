# Fibonacci

# "naive" recursive
def fib_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# list
def fib_list(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# recursive memoised
def fib_rec_memo(n, memo={0: 0, 1: 1}):
    if n not in memo:
        nth_term = fib_recursive(n - 1) + fib_recursive(n - 2)
        memo.update({n: nth_term})
    return memo.get(n)


x = 10
print("x =", x)
print("fib_recursive =", fib_recursive(x))
print("fib_list =", fib_list(x))
print("fib_fib_rec_memo =", fib_rec_memo(x))
