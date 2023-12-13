import pytest

from ayomi.use_cases.rpi import ReversePolishNotation, ReversePolishNotationError


@pytest.mark.parametrize(
    "elements", [["1", "2"], ["1", "2", "+", "-"], ["1", "2", "3", "+"]]
)
def test_npi_wrong_input(elements: list[str]) -> None:
    with pytest.raises(ReversePolishNotationError):
        ReversePolishNotation(elements).evaluate()


def test_npi_simple_sum() -> None:
    assert ReversePolishNotation(["1", "2", "+"]).evaluate() == 3


def test_npi_simple_sub() -> None:
    assert ReversePolishNotation(["1", "2", "-"]).evaluate() == -1


def test_npi_simple_mul() -> None:
    assert ReversePolishNotation(["1", "2", "*"]).evaluate() == 2


def test_npi_simple_div() -> None:
    assert ReversePolishNotation(["1", "2", "/"]).evaluate() == 0.5


def test_npi_complex_input() -> None:
    # ((10 * (6 / ((9 + 3) * -10))) + 17) + 5
    assert (
        ReversePolishNotation(
            ["10", "6", "9", "3", "+", "-10", "*", "/", "*", "17", "+", "5", "+"]
        ).evaluate()
        == 21.5
    )
