print("What numbers do you want to calculate?") 
number_1 = input()
number_1 = int(number_1)
number_2 = input()
number_2 = int(number_2)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Do you want to use additiion (+), subtraction (-), multiplication (*) or division (/)?")
choice = input()

if choice == "+":
    result_1 = add(number_1, number_2)
    print(result_1)
if choice == "-":
    result_2 = subtract(number_1, number_2)
    print(result_2)
if choice == "*":
    result_3 = multiply (number_1, number_2)
    print(result_3)
if choice == "/":
    result_4 = divide (number_1, number_2)
    print(result_4)