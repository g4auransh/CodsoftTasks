def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")

    while True:
        # Input numbers
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
        
        # Choose operation
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        operation = input("Enter the number of the operation: ")

        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        elif operation == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid operation choice! Please try again.")
            continue

        print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
