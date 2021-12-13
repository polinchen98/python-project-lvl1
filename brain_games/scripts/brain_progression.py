#!/usr/bin/env python
import prompt
from brain_games.logic import welcome_user, make_check
from brain_games.games.progression import make_progression


def main():
    exercise = 'What number is missing in the progression?'
    name = welcome_user(exercise)

    for i in range(3):
        progression, right_answer = make_progression()
        print('Question:', progression)
        answer = int(prompt.string('Your answer: '))
        if make_check(name, answer, right_answer):
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            break
