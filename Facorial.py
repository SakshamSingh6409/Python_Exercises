#This is a program to find the factorial of a inputed number using a for loop and recursion methods.

def factorial_for_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)

n=int(input("Enter a number to find its factorial: "))
print(f'Factorial using recursive method: {factorial_recursive(n)}')
print(f'Factorial using for loop method: {factorial_for_loop(n)}')
