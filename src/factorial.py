def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n == 1:
        return 1
    if n > 1:
        return factorial_recursive(n - 1) * n