from calculate import add_fun, sub_fun, mul_fun

def test_add_fun():
    assert add_fun(1, 2) == 3
    assert add_fun(-1, 1) == 0
    assert add_fun(-1, -2) == -3

def test_sub_fun():
    assert sub_fun(5, 3) == 2
    assert sub_fun(0, 1) == -1
    assert sub_fun(-1, -1) == 0

def test_mul_fun():
    assert mul_fun(2, 3) == 6
    assert mul_fun(-1, 5) == -5
    assert mul_fun(-2, -3) == 6