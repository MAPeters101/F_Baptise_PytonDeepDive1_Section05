import time

def time_it(fn, *args, rep=1, **kwargs):
    # print(args, kwargs)
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


print(time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5))

def compute_powers_1(n, *, start=1, end):
    # Using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

print(compute_powers_1(2, end=5))

def compute_powers_2(n, *, start=1, end):
    # Using a list comprehension
    return [n**i for i in range(start, end)]

print(compute_powers_2(2, end=5))

def compute_powers_3(n, *, start=1, end):
    # Using generator expression
    return (n**i for i in range(start, end))

def compute_powers_4(n, *, start=1, end):
    # Using generator expression
    return list((n**i for i in range(start, end)))

print(list(compute_powers_3(2, end=5)))
print('='*50)
print()

print(time_it(compute_powers_1, 2, start=0, end=20_000, rep=5))
print(time_it(compute_powers_2, n=2, start=0, end=20_000, rep=5))
print(time_it(compute_powers_3, n=2, start=0, end=20_000, rep=5))
print(time_it(compute_powers_4, n=2, start=0, end=20_000, rep=5))
print()

a = (2**i for i in range(5))
print(a)
print(list(a))

