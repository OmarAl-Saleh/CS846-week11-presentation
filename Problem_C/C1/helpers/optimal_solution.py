import random
import time

random.seed(42)
numbers = [random.randint(1, 100000) for _ in range(1_000_000)]

def digit_sum(n):
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total

def find_difference(numbers):
    min_num = float('inf')
    max_num = float('-inf')
    for num in numbers:
        if num < min_num or num > max_num:
            if digit_sum(num) == 30:
                min_num = min(min_num, num)
                max_num = max(max_num, num)
    return max_num - min_num

start = time.perf_counter()
result = find_difference(numbers)
elapsed = time.perf_counter() - start

print(f"Result: {result}")
print(f"Time: {elapsed:.3f}s")
