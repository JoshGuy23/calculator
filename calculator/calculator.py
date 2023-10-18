import art

# Add
def add(n1, n2):
    """Adds two numbers together."""
    return n1+n2

# Subtract
def subtract(n1, n2):
    """Subtracts a number from another number."""
    return n1-n2

# Multiply
def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1*n2

# Divide
def divide(n1, n2):
    """Divides a number by another number."""
    return n1/n2

# Stores the above functions in a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

# Main calculator function
def calculator():
    print(art.logo)
    calculating = True  # Used for the while loop
    
    # Get the first number and print the list of operations.
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while calculating:
        # Get the operation to perform and the next number.
        op = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        
        # If there is a potential divide-by-zero error, quit the function.
        if op == "/" and num2 == 0:
            print("Error: dividing by 0.")
            return 'q'

        # Call the appropriate function and store the calculation.
        function = operations[op]
        answer = function(num1, num2)

        # Display the calculation, and get ready for the next calculation.
        print(f"{num1} {op} {num2} = {answer}")
        num1 = answer

        # Ask the user whether to continue the current calculation, start a new one, or quit the program.
        cont = input(f"Type 'y' to continue calculating with {answer}, 'n' to clear calculations, or 'q' to quit: ").lower()
        if cont != "y":
            calculating = False
    return cont
 
# Continue running the calculator until the user quits or gets an error.
while True:
    status = calculator()
    if status == 'q':
        break