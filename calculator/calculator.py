import art

def add(n1, n2):
    """Adds two numbers together."""
    return n1+n2

def subtract(n1, n2):
    """Subtracts a number from another number."""
    return n1-n2

def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1*n2

def divide(n1, n2):
    """Divides a number by another number."""
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    print(art.logo)
    calculating = True

    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while calculating:
        op = input("Pick an operation")
        num2 = int(input("What's the second number?: "))

        function = operations[op]
        answer = function(num1, num2)

        print(f"{num1} {op} {num2} = {answer}")
        num1 = answer

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if cont != "y":
            calculating = False