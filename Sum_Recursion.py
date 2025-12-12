#Code that sums all the numbers to n using recursion
def sum_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + sum_recursive(n - 1)
# Example usage:
result = sum_recursive(5)
print(result)  # Output: 15 (5 + 4 + 3 + 2 + 1)
