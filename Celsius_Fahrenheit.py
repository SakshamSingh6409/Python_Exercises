#This is a code to convert temperature between Celsius and Fahrenheit

def C_to_F(c):
    f=(c*9/5)+32
    return f

def F_to_C(f):
    c=(f-32)*5/9
    return c    

t=input("Write C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if t=="C":
    c=float(input("Enter temperature in Celsius: "))
    print(f"{c}°C is equal to {C_to_F(c)}°F")
elif t=="F":
    f=float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F is equal to {F_to_C(f)}°C")
else:
    print("Invalid input. Please enter C or F.")
