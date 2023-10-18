import art

print(art.logo)

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

calculating = True

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
op = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

function = operations[op]
answer = function(num1, num2)

print(f"{num1} {op} {num2} = {answer}")

cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()
if cont != "y":
    calculating = False

while calculating:
    op = input("Pick another operation: ")
    num3 = int(input("What's the next number?: "))
    function = operations[op]
    next_answer = function(answer, num3)
    print(f"{answer} {op} {num3} = {next_answer}")
    cont = input(f"Type 'y' to continue calculating with {next_answer}, or type 'n' to exit: ").lower()
    answer = next_answer
    if cont != "y":
        calculating = False