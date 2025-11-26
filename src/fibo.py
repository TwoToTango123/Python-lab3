def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def fibo_recursive(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)
print(fibo(10), fibo_recursive(10))