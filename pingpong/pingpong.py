def is_has7(x):
    return True if x % 10 == 7 else False if x < 10 else is_has7(x // 10)


def get_direction(x):
    if x <= 1:
        return 1
    elif (x - 1) % 7 == 0 or is_has7(x - 1):
        return get_direction(x - 1) * -1
    else:
        return get_direction(x - 1)


def ping_pong(x):
    if x == 1:
        return 1
    else:
        return ping_pong(x - 1) + get_direction(x)


# print (pingpong(68))
# i = 1
# while i <= 35:
#     print(str(i) + " : " + str(pingpong(i)))
#     i += 1
# print (pingpong(998))
