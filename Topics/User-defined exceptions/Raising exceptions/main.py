class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    if (a + b) < 0:
        raise NegativeSumError(a, b)
    else:
        return a + b
