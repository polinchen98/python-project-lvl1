#!/usr/bin/env python
import prompt
from brain_games.logic import welcome_user, make_check
from brain_games.games.prime import is_prime


def main():
    exercise = '"yes" if given number is prime. Otherwise answer "no"'
    name = welcome_user(exercise)

    for i in range(3):

        right_answer, digit = is_prime()
        print('Question:', digit)
        answer = prompt.string('Your answer: ')

        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
