def discounts(x, y):
    discount = ((x - y) / x) * 100
    assert discount > 50
    return "I will buy it!"
