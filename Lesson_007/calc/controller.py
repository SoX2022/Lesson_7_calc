import view
import operation_logic


a = 0
func = ''
b = 0


def ClickButtom_v1():
    global a
    global func
    global b
    a = view.GetUserValue_v1()
    func = view.GetUserFunction()
    b = view.GetUserValue_v1()
    result = operation_logic.FunctionLogic(func, a, b)
    view.ViewData(result)


def ClickButtom_v2():
    global a
    global func
    global b
    a = view.GetUserValue_v1()
    func = view.GetUserFunction()
    while func.lower() != 'c':
        b = view.GetUserValue_v1()
        result = operation_logic.FunctionLogic(func, a, b)
        view.ViewData(result)
        a = result
        func = view.GetUserFunction()

