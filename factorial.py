num = int(input("Enter a number to find its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}")
