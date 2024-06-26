# Defining Simple arithematic functions for calculation 
from multiprocessing import Value

print("Select arithematic operation :- ")
print(  "1: Add",
        "2: Subtract",
        "3: Multiply",
        "4: Divide")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    choice = input("Enter choice(1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))

        elif choice == '3':
            print(multiply(num1, num2))

        elif choice == '4':
            print(divide(num1, num2))
        
    # Asking using to continue the operation or stop !!!
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")