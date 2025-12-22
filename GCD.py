"""Compute the greatest common divisor of a and b using the Euclidean algorithm."""
def GCD(a, b):
    while b: a, b = b, a % b
    return abs(a)


"""Compute the greatest common divisor of a and b using recursion."""
def GCD_recursive(a, b):
    return abs(a) if b == 0 else GCD_recursive(b, a % b)

# Example usage:
num1 = 48
num2 = 18
print(f"The GCD of {num1} and {num2} is {GCD(num1, num2)}")
print(f"The GCD of {num1} and {num2} using recursion is {GCD_recursive(num1, num2)}")