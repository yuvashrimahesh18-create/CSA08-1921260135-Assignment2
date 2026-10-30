
import time

# Original method: ordinary recursion
naive_calls = 0

def ways_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Redesigned method: iterative approach
iterative_calls = 0

def ways_iterative(n):
    global iterative_calls
    iterative_calls = 0

    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        iterative_calls += 1
        previous, current = current, previous + current

    return current


# Compare both methods using the same inputs
sizes = [10, 20, 25, 30]

print("ORIGINAL vs REDESIGNED")
print("----------------------")

for n in sizes:
    naive_calls = 0

    start = time.perf_counter()
    original_result = ways_naive(n)
    original_time = time.perf_counter() - start
    original_count = naive_calls

    start = time.perf_counter()
    redesigned_result = ways_iterative(n)
    redesigned_time = time.perf_counter() - start
    redesigned_count = iterative_calls

    print("\nSteps:", n)
    print("Original result:", original_result)
    print("Redesigned result:", redesigned_result)
    print("Results match:", original_result == redesigned_result)
    print("Original function calls:", original_count)
    print("Redesigned loop iterations:", redesigned_count)
    print("Original time:", original_time)
    print("Redesigned time:", redesigned_time)


# Large input test
print("\nLARGE INPUT TEST")
print("----------------")
print("Ways for 1000 steps:", ways_iterative(1000))
print("Loop iterations:", iterative_calls)
