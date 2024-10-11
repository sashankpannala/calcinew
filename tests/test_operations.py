import pytest
from app.calculator.operations import perform_operation

def test_add():
    assert perform_operation('add', 2, 3) == 5
    assert perform_operation('add', -1, 1) == 0
    assert perform_operation('add', 0, 0) == 0

def test_subtract():
    assert perform_operation('subtract', 5, 2) == 3
    assert perform_operation('subtract', 3, 3) == 0
    assert perform_operation('subtract', 2, 5) == -3

def test_multiply():
    assert perform_operation('multiply', 3, 4) == 12
    assert perform_operation('multiply', -1, 5) == -5
    assert perform_operation('multiply', 0, 10) == 0

def test_divide():
    assert perform_operation('divide', 10, 2) == 5.0
    assert perform_operation('divide', 5, 1) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        perform_operation('divide', 5, 0)

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation"):
        perform_operation('invalid', 1, 1)
