import prompt


def welcome_user(exercise):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name)
    print(exercise)

    return name


def make_check(user_name, user_answer, right_answer):
    if user_answer == right_answer:
        print('Correct!')
        return True

    print(f'{user_answer} is wrong answer ;(. '
          f'Correct answer was {right_answer}')
    print(f"Let's try again, {user_name}!'")

    return False
