def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

# Start checking from n+1
next_num = n + 1
while True:
    if is_prime(next_num):
        print(f"The next prime number after {n} is: {next_num}")
        break
    next_num += 1
