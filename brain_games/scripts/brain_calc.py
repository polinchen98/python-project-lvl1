#!/usr/bin/env python
import prompt
from random import randint
from brain_games.logic import welcome_user, make_check


def make_right_answer(digit_1, digit_2, expression):
    if expression == '+':
        return digit_1 + digit_2
    if expression == '-':
        return digit_1 - digit_2
    if expression == '*':
        return digit_1 * digit_2


def main():
    exercise = 'What is the result of the expression?'
    name = welcome_user(exercise)

    for i in range(3):

        digit_1 = randint(1, 100)
        digit_2 = randint(1, 100)
        expressions = ['+', '-', '*']
        random_expression = expressions[randint(0, len(expressions) - 1)]

        print('Question:', digit_1, random_expression, digit_2)
        answer = int(prompt.string('Your answer: '))
        right_answer = make_right_answer(digit_1, digit_2, random_expression)
        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
