
addition=2+4
subtraction=10-5
multiplication=3*7
division= 15/3
exponential=2**3
modules=15%3
floor_division=15//3
print(2+8)
print(10-5)
print(division)
print(exponential)
print(modules)
print(floor_division)


total=addition+subtraction+multiplication+division+exponential+modules+floor_division
print("********calculator********")
try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=input("Enter the operation (+, -, *, /, **, %, //): ")
    if operation=='+':
        result=num1+num2
    elif operation=='-':
        result=num1-num2
    elif operation=='*':
        result=num1*num2
    elif operation=='/':
        result=num1/num2
    elif operation=='**':
        result=num1**num2
    elif operation=='%':
        result=num1%num2
    elif operation=='//':
        result=num1//num2
    else:
        print("Invalid operation!")
        result=None
    if result is not None:        print("Result:", result)
except ValueError:
    print("Invalid input! Please enter numeric values.")