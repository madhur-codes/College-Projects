# Simple Calculator

print("1. For Addition")
print("2. For Subtraction")
print("3. For Multiplication")
print("4. For Division")
choice = int(input("Enter your choice: "))
if choice >= 1 and choice <= 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: ")) 
if choice == 1:
    print("The sum is: ", a + b)
elif choice == 2:
    print("The difference is: ", a - b)
elif choice == 3:       
    print("The product is: ", a * b)
elif choice == 4:
    if b != 0:
        print("The quotient is: ", a / b)
    else:
        print("Error: Division by zero is not allowed.")    
else:
    print("Invalid choice")  
