import model
import view
import parser


def calculate():
    input_expression()
    result = model.calculate()
    view.print_result(result)


def input_expression():
    while True:
        try:
            expr_raw = view.get_expr()
            model.expression = parser.parse(expr_raw)
            break
        except ValueError as err:
            view.error_expression(err.args[0])


def is_quit():
    while True:
        answer = view.get_is_quit()
        if answer == "y":
            return True
        if answer == "n":
            return False
