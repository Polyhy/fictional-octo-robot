def is_has(n, x):    
    return True if x % 10 == n else False if x < 10 else is_has(n, x // 10)  


def get_direction(x):
    if x < 7:
        return 1
    elif is_has(7, x) or x % 7 == 0:
        # print("%d : change direction" % (x))
        return get_direction(x - 1) * -1
    else:
        return get_direction(x - 1)


def pingpong(x):
    if x == 1:
        return 1
    else:
        return pingpong(x - 1) + get_direction(x - 1)


print(pingpong(100))