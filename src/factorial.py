def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 1 or n == 0:
        return 1
    return factorial_recursive(n - 1) * n
