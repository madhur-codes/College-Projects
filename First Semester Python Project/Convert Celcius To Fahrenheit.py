# Convert Celcius To Fahrenheit

print("1. Fahrenheit To Celcius")
print("2. Celcius To Fahrenheit")
choice = int(input("Enter your choice: "))

if choice == 1:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celcius is: ", c)
elif choice == 2:
    c = float(input("Enter temperature in Celcius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit is: ", f)
else:
    print("Invalid choice")