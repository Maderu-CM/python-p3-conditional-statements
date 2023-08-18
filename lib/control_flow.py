








def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Example usage
try:
    number = int(input("Enter a number: "))
    result = fizzbuzz(number)
    print(result)
except ValueError:
    print("Please enter a valid number.")

    

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"

# Example usage
try:
    operation = input("Enter an operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculator(operation, num1, num2)
    print(result)
except ValueError:
    print("Please enter valid numerical inputs.")

