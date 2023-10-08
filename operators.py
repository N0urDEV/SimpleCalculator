number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operator entered.")

print("The result of the operation is:", result)
