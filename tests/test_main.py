import pytest
from app.main import factorial

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_type_error():
    with pytest.raises(TypeError):
        factorial("5")

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)