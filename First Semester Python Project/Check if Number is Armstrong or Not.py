# Check if Number is Armstrong or Not

n = int(input("Enter a number: "))
a = n%10
b = (n//10)%10
c = n//100
armstrong = a**3 + b**3 + c**3
if armstrong == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")  