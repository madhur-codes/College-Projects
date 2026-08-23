# write the program to find the smallest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    min  = a
if b <= a and b <= c:   
    min = b
if c <= a and c <= b:
    min = c
print("The Smallest number is:", min)