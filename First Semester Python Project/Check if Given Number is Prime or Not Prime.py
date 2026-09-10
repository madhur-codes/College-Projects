# Program to check if the given number is prime or not
n = int(input("Enter a number: "))
if n <= 1 :
    print(n, "is not a prime number")
else:
    k = 0
    for i in range(2, n):
        if n % i == 0:
            k = 1
            break
    if k == 0:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")