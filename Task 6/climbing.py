
from functools import lru_cache

# Count function calls
naive_calls = 0
memo_calls = 0


# 1. Ordinary recursive method
def ways_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# 2. Recursive method with memoization
@lru_cache(maxsize=None)
def ways_memo(n):
    global memo_calls
    memo_calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# Test the number of ways for steps 1 to 6
print("Climbing stairs results:")

for n in range(1, 7):
    print("Steps:", n, "Ways:", ways_memo(n))



import time

# Compare both methods for different staircase sizes
sizes = [10, 20, 25, 30]

print("\nPerformance comparison:")

for n in sizes:
    # Test ordinary recursion
    naive_calls = 0
    start = time.perf_counter()
    naive_result = ways_naive(n)
    naive_time = time.perf_counter() - start

    # Test memoization
    memo_calls = 0
    ways_memo.cache_clear()

    start = time.perf_counter()
    memo_result = ways_memo(n)
    memo_time = time.perf_counter() - start

    print("\nNumber of steps:", n)
    print("Naive result:", naive_result)
    print("Naive calls:", naive_calls)
    print("Naive time:", naive_time)

    print("Memoization result:", memo_result)
    print("Memoization calls:", memo_calls)
    print("Memoization time:", memo_time)
def ways_iterative(n):
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current

# 3. Iterative method
def ways_iterative(n):
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current
print("\nLarge input test:")
print("Ways for 1000 steps:", ways_iterative(1000))
# 3. Iterative method
def ways_iterative(n):
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current