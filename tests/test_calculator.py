import pytest
from app.calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.history[-1] == "Added 2 + 3 = 5"

def test_subtract():
    assert Calculator.subtract(5, 2) == 3
    assert Calculator.history[-1] == "Subtracted 5 - 2 = 3"

def test_multiply():
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.history[-1] == "Multiplied 3 * 4 = 12"

def test_divide():
    assert Calculator.divide(10, 2) == 5.0
    assert Calculator.history[-1] == "Divided 10 / 2 = 5.0"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.divide(5, 0)

def test_square():
    assert Calculator.square(4) == 16
    assert Calculator.history[-1] == "Squared 4 = 16"

def test_cube():
    assert Calculator.cube(3) == 27
    assert Calculator.history[-1] == "Cubed 3 = 27"

def test_get_last_calculation():
    Calculator.clear_history()
    Calculator.add(1, 1)
    assert Calculator.get_last_calculation() == "Added 1 + 1 = 2"

def test_clear_history():
    Calculator.clear_history()
    Calculator.add(1, 2)
    assert len(Calculator.history) == 1
    Calculator.clear_history()
    assert len(Calculator.history) == 0
