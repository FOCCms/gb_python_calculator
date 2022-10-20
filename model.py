operations = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}

expression = []


def delete_element(expr, i):
    expr.pop(i + 1)
    expr.pop(i)


def make_operation(expr, i, operation):
    if expr[i] == operation:
        expr[i - 1] = operations.get(operation)(int(expr[i - 1]), int(expr[i + 1]))
        delete_element(expr, i)
        return True


def calculate():
    global expression
    while len(expression) > 1:
        if '*' in expression or '/' in expression:
            for i in range(len(expression)):
                if make_operation(expression, i, '*'):
                    break
                if make_operation(expression, i, '/'):
                    break

        elif '+' in expression or '-' in expression:
            for i in range(len(expression)):
                if make_operation(expression, i, '+'):
                    break
                if make_operation(expression, i, '-'):
                    break
    return expression[0]
