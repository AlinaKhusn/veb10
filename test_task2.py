import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
            pytest.param(2, 2, 1, marks=pytest.mark.skip('Не проверяем')),
            pytest.param(10, 5, 2, marks=pytest.mark.smoke)
            ],
                         ids=['positive', 'smoke'])

def test_integer(a, b, result):
    assert all_division(a, b) == result


def test_float():
    assert all_division(5, 2) == 2.5


def test_negative():
    assert all_division(2, 2) == 0


def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(2, 0)


def test_negative_letter():
    with pytest.raises(TypeError):
        assert all_division(10, 'asd'), 'Передана строка'