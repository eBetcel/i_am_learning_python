from typing import Callable, Dict
from numbers import Number

func = lambda: 'resultado da funcao'


calc: Dict[str, Callable] = {
    'soma': lambda x, y: x - y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y
}

def soma(x: Number, y: Number) -> Number:
    """
    Args:
        x: Number
        y: Number
    Returns: Number
    """
    return x + y

calc: Dict[str, Callable] = {
    'soma': soma,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y
}