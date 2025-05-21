import os
from dotenv import load_dotenv

load_dotenv()

def factorial(n):
    """Обчислює факторіал числа n (n!)"""
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом")
    if n < 0:
        raise ValueError("Аргумент має бути невід'ємним")
    return 1 if n == 0 else n * factorial(n - 1)