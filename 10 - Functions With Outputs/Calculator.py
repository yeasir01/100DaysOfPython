import art

#Build your functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)

    finished = False
    total = float(input("Whats the first number?: "))

    #Print different operation types
    for key in operations:
        print(key)

    while not finished:
        selected_op = input("What operation would you like to perform?: ")
        next_num = float(input("Whats the next number?"))
        op_function = operations[selected_op]
        new_total = op_function(total, next_num)
        print(f"{total} {selected_op} {next_num} = {new_total}")
        
        answer = input(f'Type "Y" to continue calculating with {new_total}, "N" to start a new calculation or "E" to exit: ').lower()

        if answer == "y":
            total = new_total
        elif answer == "e":
            finished = True
            break
        else:
            finished = True
            calculator() #recursion

calculator()