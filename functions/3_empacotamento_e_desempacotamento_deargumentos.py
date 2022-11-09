"""Desempacotamento de argumentos"""


def sum(*args):
    """args empacota e desempacota como uma tupla"""
    return sum(args)


def sum(x, y, *args):
    """também funciona"""
    return sum(args)

#def meu_sum(*args, **kwargs):
def meu_sum(*grupo_pos, **grupo_nomeado):
    """grupo_pos cria uma tupla e grupo_nomeado cria um dict"""
    return grupo_pos, grupo_nomeado
