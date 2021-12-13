#!/usr/bin/env python
import prompt
from brain_games.logic import welcome_user, make_check
from brain_games.games.calc import make_right_answer


def main():
    exercise = 'What is the result of the expression?'
    name = welcome_user(exercise)

    for i in range(3):
        right_answer, digit_1, digit_2, expression = make_right_answer()
        print('Question:', digit_1, expression, digit_2)
        answer = int(prompt.string('Your answer: '))
        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
