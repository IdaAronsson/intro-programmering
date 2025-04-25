import math

def digit_factorial_sum(n):
    return sum(math.factorial(int(d)) for d in str(n))

results = []
for i in range(10, 2540161):
    if i == digit_factorial_sum(i):
        results.append(i)

print("Sum:", sum(results))