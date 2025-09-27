def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exponent")

while True:
    choice = input("select 1/2/3/4/5 = ")

    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == '5':
        print(num1, "exponent", num2, "=", pow(num1, num2))

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if  next_calculation == "no":
        print("Exiting calculator")
        break
    else:
        print("next calculation")