def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        a, b = 0, 1
        while len(series) < n:
            next_num = a + b
            series.append(next_num)
            a = b
            b = next_num
        return series

# Example: Get first 10 Fibonacci numbers
print(fibonacci_iterative(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
