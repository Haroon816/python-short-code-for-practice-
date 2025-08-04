#check about adam number is present or not 
num=int(input("Enter a number for square:- ="))
sqr= num*num;
print(f"Square number :: == {sqr}")
reversed_num = int(str(num)[::-1])
print(f"this is your reverse numbr := {reversed_num}")
rev_num = int(reversed_num)
sqr2 = rev_num*rev_num
print(f"The Square of reverse number := {sqr2}")
sqr2=str(sqr2)
rev_sq_num = int(str(sqr2[::-1]))
print(f"The reverse of square of new number is  := {rev_sq_num}")
if(sqr == rev_sq_num):
    print(f"Hence proved both number {num} and {rev_num} are Adam Number.")
else:
    print("sorry , both are not Adam Numbers!")