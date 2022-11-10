""""
# High order functions
1. Recebe uma função
2. Retorna uma função
3. Um ou outro
"""

soma_2 = lambda val: val + 2


from typing import Callable, Any

def reaplica(func: Callable, val: Any) -> Any:
    """Função que reaplica o resultado da chamada"""
    return func(
        func(val)
    )