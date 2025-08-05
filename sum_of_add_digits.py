# Ask the user to enter a number
num = int(input("Enter a number: "))

# Initialize sum variable
digit_sum = 0

# Use while loop to extract and add digits
while num > 0:
    digit = num % 10      # Get the last digit
    digit_sum += digit    # Add it to the sum
    num = num // 10       # Remove the last digit

# Print the result
print("Sum of digits is:", digit_sum)
