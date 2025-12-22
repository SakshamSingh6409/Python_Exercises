def GCD(a,b):
    """Compute the greatest common divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)


def GCD_recursive(a, b):
    """Compute the greatest common divisor of a and b using recursion."""
    if b == 0:
        return abs(a)
    else:
        return GCD_recursive(b, a % b)

# Example usage:
if __name__ == "__main__":  
    num1 = 48
    num2 = 18
    print(f"The GCD of {num1} and {num2} is {GCD(num1, num2)}")
    print(f"The GCD of {num1} and {num2} using recursion is {GCD_recursive(num1, num2)}")