from random import randint


def is_prime():
    a = randint(1, 1000)
    for i in range(2, a - 1):
        if a % i == 0:
            return 'no', a
    return 'yes', a
