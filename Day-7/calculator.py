def  addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
def floor_division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a // b
def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")

    choice = input("Enter choice (1-7): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {addition(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '6':
            print(f"{num1} ** {num2} = {exponentiation(num1, num2)}")
        elif choice == '7':
            print(f"{num1} // {num2} = {floor_division(num1, num2)}")
    else:
        print("Invalid input")
if __name__ == "__main__":
    calculator()# Simple calculator program that performs basic arithmetic operations   
        