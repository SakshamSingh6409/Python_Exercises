#A code to find is a number is even or odd using bitwise operator
def even_or_odd_bitwise(num):
    if num & 1 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    even_or_odd_bitwise(num)