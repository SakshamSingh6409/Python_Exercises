#This program checks whether a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    even_or_odd(num)
