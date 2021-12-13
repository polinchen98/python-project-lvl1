from random import randint


def is_even():
    digit = randint(1, 100)
    if digit % 2 == 0:
        return 'yes', digit
    return 'no', digit
