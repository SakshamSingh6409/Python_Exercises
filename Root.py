#this is a program to find the perfect square root of any number and if the number is not a perfect square it will return "Not a perfect square"
from math import *
n=int(input())
def root_loop(n):
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

def root_inbuilt(n):
    a=sqrt(n)
    if a==int(a):
        return int(a)
    else:
        return "Not a perfect square"

print(f"Finding the root using loop: {root_loop(n)}")
print(f"Finding the root using inbuilt function: {root_inbuilt(n)}")