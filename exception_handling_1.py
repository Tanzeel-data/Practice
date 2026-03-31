# try:
#     # Taking input from user
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
    
#     # Performing division
#     result = num1 / num2
    
#     print("Result:", result)

# except ValueError:
#     print("Invalid input! Please enter numbers only.")

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# except Exception as e:
#     print("Something went wrong:", e)

# finally:
#     print("Execution completed.")
try:
    num = int(input("Enter a number between 1 and 10: "))
    
    if num < 1 or num > 10:
        raise ValueError("Number must be between 1 and 10.")
    
    print("Valid number:", num)

except ValueError as e:
    print("Error:", e)   