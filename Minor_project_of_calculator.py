# Minor project of calculator 
operator = input("Enter your % operator:= ")

if(operator == "+"):
    num = int(input("How much number you want to add :="))
    sum=0
    for i in range(num):
        result = int(input(f"Enter your number {i+1} := "))
        sum += result
    print(sum)
elif(operator == "-"):
   num = int(input("How many numbers you want to enter? "))
   if num > 0:
       first = int(input("Enter number 1: "))
       result = first
       for i in range(1, num):
           next_num = int(input(f"Enter number {i+1}: "))
           result -= next_num
           print("Final result after subtraction:", result)
elif(operator == "*"):
    num = int(input("How much number you want to Multiple :="))
    Mul = 1
    for i in range(num):
        result = int(input(f"Enter your number {i+1} := "))
        Mul *= result
    print(Mul)
elif(operator == "/"):
    num = int(input("How many numbers you want to divide? "))

if num > 0:
    Div = int(input("Enter number 1: "))  # Take the first number as starting value

    for i in range(1, num):
        next_num = int(input(f"Enter number {i+1}: "))
        if next_num == 0:
            print("Division by zero is not allowed.")
            break
        Div /= next_num

    else:
        print("Final division result is:", Div)
else:
    print("You must enter at least one number.")




    