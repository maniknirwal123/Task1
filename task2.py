# Function to perform basic arithmetic operations
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Main program
def main():
    print("Simple Calculator")
    print("------------------")
    
    # Get user input for the two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Display the operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get the user's choice of operation
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform the calculation
    result = calculate(num1, num2, operation)
    
    # Display the result
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
