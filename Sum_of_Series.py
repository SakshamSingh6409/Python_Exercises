# this code will give the sum of the series $1^3+2^3+.....+n^3$
def sum_of_series(n):
    series_sum = 0
    for i in range(1, n+1):
        series_sum = series_sum+ (i**3)
    return series_sum

n = int(input("Enter a positive integer n: "))
print(f"Sum of series up to {n} is: {sum_of_series(n)}")
