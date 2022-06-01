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
        return 'blues screen of the death'


print(calculator(operator[0], 1000, 2000))
