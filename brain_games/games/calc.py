def make_right_answer(digit_1, digit_2, expression):
    if expression == '+':
        return digit_1 + digit_2
    if expression == '-':
        return digit_1 - digit_2
    if expression == '*':
        return digit_1 * digit_2
