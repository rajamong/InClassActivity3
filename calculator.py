# addition function
def addition(num1, num2):
    return num1 + num2

# subtraction function
def subtraction(num1, num2):
    return num1 - num2

# multiplication function
def multiplication(num1, num2):
    return num1 * num2

# division function
def division(num1, num2):
    return num1 / num2


while True:

    # take in the users inputs
    num1 = float(input("pls enter your first number: "))
    num2 = float(input("pls enter your second number: "))

    # prints out all of the calculations
    print(num1, "+", num2, "=", addition(num1, num2))
    print(num1, "-", num2, "=", subtraction(num1, num2))
    print(num1, "*", num2, "=", multiplication(num1, num2))
    print(num1, "/", num2, "=", division(num1, num2))
