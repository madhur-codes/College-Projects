# Find Reverse Of a Three Digits Number


n = int(input("Enter a three digits number : "))
a = n%10
n = n//10
b = n%10
n = n//10
c = n
reverse = a*100 + b*10 + c
print("The reverse of the number is : ", reverse)
