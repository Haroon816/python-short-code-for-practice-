# Ask user to enter a number
num = int(input("Enter a number: "))

# Initialize sum and counter
total = 0
i = 1

# Use while loop to calculate the sum
while i <= num:
    total += i
    i += 1

# Display the result
print(f"The sum of numbers from 1 to {num} is: {total}")
