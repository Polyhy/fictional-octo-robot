def get_direction(x):
    if x < 7:
        return 1
    elif x % 10 == 7 or x % 7 == 0:
        return get_direction(x - 1) * -1
    else:
        return get_direction(x - 1)


def pingpong(x):
    if x == 1:
        return 1
    else:
        return pingpong(x - 1) + get_direction(x - 1)
