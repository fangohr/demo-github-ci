def f(n):                     # "production code"
    s = 0
    # Loop from 0 to n:
    for i in range(1, n + 1):
        s = s + i 
    return s


def test_f():                 # "test code"
    assert f(3) == 0 + 1 + 2 + 3
    assert f(5) == 15
    assert f(10) == 55
