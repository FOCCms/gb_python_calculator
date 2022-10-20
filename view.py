import logger


def get_expr():
    expr_raw = input("Введите выражение: ")
    logger.logger(f"Введите выражение: {expr_raw}")
    return expr_raw


def error_expression(err):
    logger.logger(f"Ошибка: {err}")
    print(f"Ошибка: {err}")


def print_result(result):
    logger.logger(f'Результат: {result}')
    print(f'Результат: {result}')


def get_is_quit():
    answer = input("Закончить выполнение программы? (y/n): ")
    logger.logger(f"Закончить выполнение программы? (y/n): {answer}")
    return answer
