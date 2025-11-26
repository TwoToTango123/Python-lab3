def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quick_sort(a: list[int]) -> list[int]:
    if len(a) <= 1:
        return a
    else:
        pivot = a[-1]
        left = [x for x in a[:-1] if x < pivot]  
        right = [x for x in a[:-1] if x >= pivot]  
        return quick_sort(left) + [pivot] + quick_sort(right)  

def counting_sort(a: list[int]) -> list[int] :
    if not a:
        return a

    min_val, max_val = min(a), max(a)
    range_size = max_val - min_val + 1
    count = [0] * range_size

    for num in a:
        count[num - min_val] += 1

    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])

    return result

def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return a
    max_num = max (a)
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in a:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        a = [num for bucket in buckets for num in bucket]
        exp *= base
    return a

def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return a

    n = len(a)
    buckets = [[] for _ in range(n)]

    for x in a:
        buckets[int(x * n)].append(x)

    for bucket in buckets:
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key

    result = []
    for bucket in buckets:
        result.extend(bucket)

    return result

def heap_sort(a: list[int]) -> list[int]:
    n = len(a)

    for start in range(n // 2 - 1, -1, -1):
        parent = start
        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            largest = parent

            if left < n and a[left] > a[largest]:
                largest = left
            if right < n and a[right] > a[largest]:
                largest = right

            if largest == parent:
                break

            a[parent], a[largest] = a[largest], a[parent]
            parent = largest

    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        parent = 0
        while True:
            left = 2 * parent + 1
            right = 2 * parent + 2
            largest = parent

            if left < end and a[left] > a[largest]:
                largest = left
            if right < end and a[right] > a[largest]:
                largest = right

            if largest == parent:
                break

            a[parent], a[largest] = a[largest], a[parent]
            parent = largest

    return a