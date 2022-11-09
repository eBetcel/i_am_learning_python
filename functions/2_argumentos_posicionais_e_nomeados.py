def anomina(param): return param + 2


def anomina_plus(param1, param2): return param1 + param2

# call anonima_plus(1, 2)


def soma_pos(x, y):
    """
    x e y são parâmetros posicionais
    """
    return x + y


def soma_nomeados(x=4, y=4):
    """
    x e y são parametros nomeados.
    na falta de x ou y, o valor 7 será usado
    """
    return x + y


def soma_explicitamente_nomeados(*, x=4, y=4):
    """
    x e y são parametros nomeados.
    na falta de x ou y, o valor 7 será usado
    o * faz com que a tudo que venha depois dele só receba parametros nomeados
    """
    return x + y


def soma_explicitamente_nomeados_2(x=4, *, y=4):
    """
    x e y são parametros nomeados.
    na falta de x ou y, o valor 7 será usado
    o * faz com que a tudo que venha depois dele só receba parametros nomeados
    """
    return x + y


def soma_explicitamente_posicional(x=4, /, y=4):
    """
    x e y são parametros nomeados.
    na falta de x ou y, o valor 7 será usado
    o / faz com que a tudo que venha antes dele só receba parametros posicionais
    """
    return x + y


def soma_tudo_mix(x, y, /, z, *, w):
    return sum((x, y, z, w))
