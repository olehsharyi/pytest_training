from src.main import A, Calculator
import pytest
from contextlib import nullcontext

# def test_sum():
#     x = 1
#     y = 3
#     assert x + y == 4
#
#
# def test_main():
#     assert A.x == 1
#
#
# def test_second():
#     assert 2 == 2


class TestCalculator:
    @pytest.mark.parametrize("x, y, res, expectation", [
        (1, '0', 0.5, pytest.raises(TypeError)),
        (5, -1, -5, nullcontext())
    ])
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res


    @pytest.mark.parametrize('x, y, res', [(1, 2, 3), (5, -1, 4)])
    def test_add(self, x, y, res):
        assert Calculator().add(x, y) == res
