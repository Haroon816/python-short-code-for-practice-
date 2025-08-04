num = int(input("Enter a number to check if it's prime: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("The number is a prime number")
    else:
        print("The number is not a prime number")
