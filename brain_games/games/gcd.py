def find_gcd(digit_1, digit_2):
    while digit_1 != 0 and digit_2 != 0:
        if digit_1 > digit_2:
            digit_1 = digit_1 % digit_2
        else:
            digit_2 = digit_2 % digit_1
    return digit_1 + digit_2
