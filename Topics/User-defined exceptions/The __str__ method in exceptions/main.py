def check_integer(num):
    if not 45 < num < 67:
        raise NotInBoundsError(num)
    else:
        print(num)


def error_handling(num):
    try:
        check_integer(num)
    except NotInBoundsError as err:
        print(err)
