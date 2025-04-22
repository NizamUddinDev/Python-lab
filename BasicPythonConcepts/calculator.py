num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
operator = input("Enter operation: +, -, *, /")
if operator == "+":
    print(f"the sum is {num1 + num2}")
elif operator == "-":
    print(f"The difference is {num1-num2}")
elif operator == "*":
    print(f"The multiplication is {num1*num2}")
elif operator == "/":
    print(f"The division is {num1/num2}")
else:
    print("f{operator} is invalid: ")