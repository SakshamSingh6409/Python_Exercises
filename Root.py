#this is a program to find the perfect square root of any number and if the number is not a perfect square it will return "Not a perfect square"
n=int(input())
def root(n):
    r=True
    a=0
    while r:
        a+=1
        if a*a==n:
            r=False
        elif a*a>n:
            a="Not a perfect square"
            r=False
    return a
print(root(n))