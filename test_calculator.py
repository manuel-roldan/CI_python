import calculator

def test_sum():
    assert calculator.sum(2, 3) == 5

def test_div():
    assert calculator.div(6, 2) == 3

def test_mul():
    assert calculator.mul(2, 3) == 6

def test_dif():
    assert calculator.dif(3, 2) == 1