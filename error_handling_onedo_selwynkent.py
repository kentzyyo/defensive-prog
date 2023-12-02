import math

# selwyn kent onedo
# Dictionary to store previous calculation results
results = {}

# Loop to continuously run the calculator
while True:
    try:
        # Prompt user to input the first number or 'q' to quit
        first_number = input("Enter the first number (or 'q' to quit): ")
        
        # Check if user wants to quit
        if first_number.lower() == 'q':
            break
        
        # Convert the input to a floating-point number
        first_number = float(first_number)
        
        # Prompt user to input the operation to perform
        operation = input("Enter the operation (+, -, *, /, ** for exponentiation, sqrt for square root): ")
        
        # Check if the entered operation is valid
        if operation not in ['+', '-', '*', '/', '**', 'sqrt']:
            raise ValueError("Invalid operation entered!")
        
        # Check for square root operation and if the first number is negative
        if operation == 'sqrt' and first_number < 0:
            raise ValueError("Cannot calculate square root of a negative number!")
        
        # Prompt user to input the second number
        second_number = float(input("Enter the second number: "))
        
        # Check for division by zero
        if operation == '/' and second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")
        
        result = None
        
        # Perform the calculation based on the selected operation
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            result = first_number / second_number
        elif operation == '**':
            result = first_number ** second_number
        elif operation == 'sqrt':
            result = math.sqrt(first_number)
        
        # Store the calculation result in the dictionary
        results[(first_number, operation, second_number)] = result
        print("\nResult:", result)
    
    # Catch ValueError exceptions
    except ValueError as ve:
        print(f"\nError: {ve}")
    
    # Catch ZeroDivisionError exceptions
    except ZeroDivisionError as zde:
        print(f"\nError: {zde}")
    
    # Catch other exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    # Finally block always executed whether an exception occurred or not
    finally:
        print("This block is executed whether an exception occurred or not.\n")

# Displaying previous results stored in the dictionary
print("\nPrevious Results:")
for key, value in results.items():
    print(f"{key} = {value}")
