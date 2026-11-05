# Find Factorial Using Function
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)

num = int(input("Enter a number: "))
print("The factorial of", num, "is", find_factorial(num))