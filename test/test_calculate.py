from calculate import add_fun

def test_add_fun():
    assert add_fun(1, 2) == 3
    assert add_fun(-1, 1) == 0
    assert add_fun(-1, -2) == -3