#Calculator.py
# Programme module provides basic arithmetic operations.
def add(x, y):
#Return the sum of x and y.
    return x + y
def subtract(x, y):
    #Return the difference of x and y.
    return x - y  
def multiply(x, y):
    #Return the product of x and y.
    return x * y
def divide(x, y):
    #Return the quotient of x and y.
    if y != 0:
        return x / y
    else:
        return "Division by zero error" 
    
#ask the user for input and perform the operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

#call the functions
if __name__ == "__main__":
    calculator()