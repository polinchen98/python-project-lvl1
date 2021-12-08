import prompt
from random import randint


def is_even(digit):
    if digit % 2 == 0:
        return 'yes'
    return 'no'


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        digit = randint(1, 100)
        print('Question:', digit)
        answer = prompt.string('Your answer: ')
        if answer == 'yes' or answer == 'no':
            if is_even(digit) != answer:
                print(answer, 'is wrong answer ;(. Correct answer was', is_even(digit))
                print(f"Let's try again, {name}!'")
                break
            else:
                print('Correct!')
                if i == 2:
                    print(f'Congratulations, {name}!')
        else:
            print(answer, 'is wrong answer ;(. Correct answer was', is_even(digit))
            print(f"Let's try again, {name}!'")
            break

