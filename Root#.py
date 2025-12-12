'''n=int(input())
def root(n):
    a=[]
    for i in range(1, int(n/2)+1):
        is_perfect = True
        for j in range(1, i):
            if i*j != n:
                is_perfect = False
                break
        if is_perfect:
            a.append(i)

    for i in a:
        if n%i==0:
            return i

print(root(n))'''
'''
n=int(input())
def root(n):
    print(n**0.5)

for i in range(1, n+1):
    root(i)
'''

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