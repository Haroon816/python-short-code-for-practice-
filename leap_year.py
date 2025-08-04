Years = int(input("Enter the Year := "))
if(Years % 4 == 0):
    if(Years % 100 == 0):
        if(Years % 400 == 0):
            print(f"This is Leap {Years}")
        else:
            print("This is not Leap Years")
    else:
        print("This is not Leap Years")
else:
    print("This is not Leap Years")