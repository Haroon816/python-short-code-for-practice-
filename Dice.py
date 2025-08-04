face = int(input("Enter the number on the dice face (1 to 6): "))

if face == 1:
    opposite = 6
elif face == 2:
    opposite = 5
elif face == 3:
    opposite = 4
elif face == 4:
    opposite = 3
elif face == 5:
    opposite = 2
elif face == 6:
    opposite = 1
else:
    print("Invalid input! Please enter a number between 1 and 6.")
    opposite = None

if opposite is not None:
    print(f"The number on the opposite face is: {opposite}")
