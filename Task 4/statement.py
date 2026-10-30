import time
# Method 1: Building a statement using repeated +

def build_plus(parts):
    result = ""

    for part in parts:
        result += part + ";"

    return result
parts = ["Milk", "Rice", "Sugar"]

print("Repeated + method:")
print(build_plus(parts))

# Method 2: Building a statement using join()

def build_join(parts):
    return ";".join(parts) + ";"
print("Join method:")
print(build_join(parts))

# Method 3: Building a statement using f-strings

def build_fstring(parts):
    result = ""

    for part in parts:
        result += f"{part};"

    return result
print("F-string method:")
print(build_fstring(parts))


# Performance comparison using 3 runs and average time

sizes = [1000, 10000, 200000]

for size in sizes:
    parts = [f"Item{i}" for i in range(size)]

    print("\nNumber of items:", size)

    for name, function in [
        ("Repeated +", build_plus),
        ("Join", build_join),
        ("F-string", build_fstring)
    ]:
        times = []

        for run in range(3):
            start = time.perf_counter()
            function(parts)
            elapsed = time.perf_counter() - start
            times.append(elapsed)

        average = sum(times) / len(times)

        print(name, "average time:", average)
