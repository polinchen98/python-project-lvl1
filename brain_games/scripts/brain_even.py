#!/usr/bin/env python
import prompt
from random import randint
from brain_games.logic import welcome_user, make_check
from brain_games.games.even import is_even


def main():
    exercise = 'Answer "yes" if the number is even, otherwise answer "no".'
    name = welcome_user(exercise)

    for i in range(3):
        digit = randint(1, 100)
        print('Question:', digit)
        answer = prompt.string('Your answer: ')
        right_answer = is_even(digit)
        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
