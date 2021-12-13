from random import randint


def make_right_answer():
    digit_1 = randint(1, 100)
    digit_2 = randint(1, 100)
    expressions = ['+', '-', '*']
    random_expression = expressions[randint(0, len(expressions) - 1)]

    if random_expression == '+':
        return digit_1 + digit_2, digit_1, digit_2, random_expression
    if random_expression == '-':
        return digit_1 - digit_2, digit_1, digit_2, random_expression
    if random_expression == '*':
        return digit_1 * digit_2, digit_1, digit_2, random_expression
