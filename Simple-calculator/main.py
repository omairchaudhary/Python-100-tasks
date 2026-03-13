# calculator.py

num1 = float(input("Enter First Number: "))
num2 = float(input("enter 2nd Number: "))

operation = input("Enter Operation (+,-,*,/): ")


if operation == "+":
    result = num1 + num2
    
elif operation == "-":
    result = num1 - num2
    
elif operation == "*":
    result = num1 * num2
    
elif operation == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result = "Error! Division by zero"
else:
    result = "invalid operation"
    
print(f"Result: {result}")