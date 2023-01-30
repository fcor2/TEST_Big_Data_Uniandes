# define calculator operations

def calculator(a, b, operation):
    if (a.isnumeric()) & (b.isnumeric()):
        a, b = float(a), float(b)
        if operation == 'suma':
            result = a + b
        elif operation == 'resta':
            result = a - b
        elif operation == 'mult':
            result = a * b
        elif operation == 'div':
            result = a / b
        else:
            result = 'Error: Solo soporta suma, resta, multiplicación y división.'
    else:
            result = 'Ingrese solo números.'
    
    return result


# a = input('First number\n')
# b = input('Second number\n')
# operation = input('Operation\n')

# print(calculator(a, b, operation))
