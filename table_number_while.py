#write a program enter a number print that number table by using while loop 
table = int(input("Enter Your TAble number = "))
n=1
while(n <= 10):
    print(f"{table} * {n} = {table * n}")
    n=n++1
print(f"/n /n Thank you so much ! this is the Table of {table}")