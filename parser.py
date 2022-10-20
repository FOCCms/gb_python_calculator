import re


def parse(expr_raw: str):
    expr_raw = expr_raw.replace(' ', '').strip()

    find_non_valid_symbols(expr_raw)

    expr = expr_raw \
        .replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ') \
        .split()

    check_operands_order(expr)

    return expr


def check_operands_order(expr):
    is_digit = True
    for operand in expr:
        if is_digit and not operand.isdigit():
            raise ValueError("В выражении нарушен порядок операндов")
        if not is_digit and operand.isdigit():
            raise ValueError("В выражении нарушен порядок операндов")
        is_digit = not is_digit


def find_non_valid_symbols(expr_raw):
    search = re.compile(r'[^\d\\+\\/\\*\\-]+').search
    if bool(search(expr_raw)):
        raise ValueError("Выражение не распознано")
