#!/usr/bin/env python
import prompt
from random import randint
from brain_games.logic import welcome_user, make_check
from brain_games.games.gcd import find_gcd


def main():
    exercise = 'Find the greatest common divisor of given numbers.'
    name = welcome_user(exercise)

    for i in range(3):
        digit_1 = randint(1, 100)
        digit_2 = randint(1, 100)
        print('Question:', digit_1, digit_2)
        answer = int(prompt.string('Your answer: '))
        right_answer = find_gcd(digit_1, digit_2)
        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
