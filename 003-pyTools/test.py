operator = ['+', '-', '*', '/']

def calculator(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'blue screen of the death'

print(calculator(operator[0], 10, 20))