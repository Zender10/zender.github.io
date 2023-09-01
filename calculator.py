#Most simplese python caluclator!!

# Define a dictionary to map operators to functions
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

# Input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Check if the operator is valid
if operator in operators:
    result = operators[operator](num1, num2)
    print(f"Result: {result}")
else:
    print("Invalid operator")
