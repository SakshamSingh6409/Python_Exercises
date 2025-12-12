from numpy import *

a = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a[1, 1:])

# Determinant of a matrix = 00(11*22 - 12*21) - 01(10*22 - 12*20) + 02(10*21 - 11*20)

for i in range(3):
    for j in range(3):
        print(a[0, j])