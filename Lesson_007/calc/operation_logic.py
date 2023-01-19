import functions


def FunctionLogic(operation, x, y):
    if operation == '+':
        return functions.PlusFunction(x, y)
    elif operation == '-':
        return functions.MinusFunction(x, y)
    elif operation == '*':
        return functions.MultiplicationFunction(x, y)
    elif operation == '/':
        return functions.DivisionFunction(x, y)

