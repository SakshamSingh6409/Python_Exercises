import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Determinant of a matrix = 00(11*22 - 12*21) - 01(10*22 - 12*20) + 02(10*21 - 11*20)
def det1(a):
    for i in a[0, :]:
        for j in range(3):
            f=i*a[1, (j+1)%3]*a[2, (j+2)%3]
            s=i*a[1, (j+2)%3]*a[2, (j+1)%3]
            det=f-s
            return det

def det2(m):
    return m[0][0] if len(m) == 1 else sum(  # This now works as expected
        (-1)**j * m[0][j] * det2([r[:j] + r[j+1:] for r in m[1:]])
        for j in range(len(m))
    )

def det3(mat):
    n = len(mat)          # matrix size (n x n)

    # base cases
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

    det = 0
    # expand along first row using loops
    for col in range(n):
        # build the (n-1)x(n-1) minor matrix by skipping row 0 and column col
        minor = []
        for r in range(1, n):
            row = []
            for c in range(n):
                if c == col:
                    continue
                row.append(mat[r][c])
            minor.append(row)

        sign = 1 if col % 2 == 0 else -1
        det += sign * mat[0][col] * det3(minor)

    return det

def det4(m):
    # m is a 3x3 list of lists
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    
    return (
        a * (e * i - f * h)
        - b * (d * i - f * g)
        + c * (d * h - e * g)
    )

print("Determinant of the matrix is:", np.linalg.det(a))
print("Determinant calculated using recursion is:", det2(a.tolist()))
print("Determinant calculated using loop expansion is:", det3(a.tolist()))
print("Determinant calculated using direct formula is:", det4(a.tolist()))