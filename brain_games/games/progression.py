from random import randint


def make_progression():
    a_1 = randint(1, 10)
    d = randint(1, 10)
    x = randint(5, 10)
    progression = []
    for i in range(x):
        a_1 = a_1 + d
        progression.append(a_1 + d)
    a_n_index = randint(0, x - 1)
    missed_digit = progression[a_n_index]
    progression[a_n_index] = '..'
    progression = [str(x) for x in progression]
    return ' '.join(progression), missed_digit
