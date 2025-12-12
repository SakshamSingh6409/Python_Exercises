# This program finds all prime factors of a given number
def factorial(n):
    a=[]
    for i in range(2, int(n/2) + 1):
        is_prime = True          # <--- The Flag
        for j in range(2, i):
            if i % j == 0:
                is_prime = False # Found a divisor, so NOT prime
                break            # Stop checking this number
        if is_prime:             # Only append AFTER the inner loop finishes
            a.append(i)
            
    fac=[]
    for i in a:
        if n%i==0:
            fac.append(i)
    return fac

if __name__ == "__main__":
    n=int(input())
    print(factorial(n))