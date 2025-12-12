# Code that finding the biggest number among three numbers and determins if the biggest number is odd or even, using conditional commands
def bigger_of_three(a, b, c):
    if a >= b and a >= c:
        biggest = a
    elif b >= a and b >= c:
        biggest = b
    else:
        biggest = c

    if biggest % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    return biggest, parity

if __name__ == "__main__":
    num1, num2, num3 = map(int, input("Enter three numbers separated by spaces: ").split())
    biggest, parity = bigger_of_three(num1, num2, num3)
    print(f"The biggest number is {biggest} and it is {parity}.")
    