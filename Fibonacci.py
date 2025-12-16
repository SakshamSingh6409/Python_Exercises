#this is a programe that finds a fibunaccci sequence up to the user defined number n using loop method and recursion method

a = 0
l=[]
def fibonacci_loop(n):
    a = 0
    b = 1
    
    # Check if n is less than 0
    if n < 0:
        print("Incorrect input")
        
    # Check if n is equal to 0
    elif n == 0:
        l.append(0)
      
    # Check if n is equal to 1
    elif n == 1:
        l.append(1)
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
            l.append(b)

def fibonacci_recursive(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        print(result)
        return result

fibonacci_loop(9)
print(l)
fibonacci_recursive(9)