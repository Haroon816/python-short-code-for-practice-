num1 = int(input("Enter the first number ="))
num2 =  int(input("Enter the second number ="))
num3 =  int(input("Enter the third number ="))

if (num1 > num2) and (num1 > num3):
    print(f"This first number is greatest = {num1}")
elif (num2 > num1) and (num2 > num3):
    print(f"This second number is greatest = {num2}")
elif (num3 > num1) and (num3 > num2):
    print(f"This third number is greatest = {num3}")
else:
    print(f"Two or more numbers are equal and greatest among: {num1}, {num2}, {num3}")
