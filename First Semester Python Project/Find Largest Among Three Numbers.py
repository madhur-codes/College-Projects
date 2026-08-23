# write the program to find the Largest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    max = a
if b >= a and b >= c:   
    max = b
if c >= a and c >= b:
    max = c
print("The Largest number is:", max)