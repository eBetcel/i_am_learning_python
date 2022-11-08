# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
def zero_to_ten():
    n = -1
    while (n < 0 and n > 10):
        n = int(input())
    return True

# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.


def fibonacci(n: int):
    x1 = 1
    x2 = 1
    aux = 0

    if n == 1:
        print(1)

    elif n > 1:
        print(1)
        print(1)
        for i in range(n - 2):
            aux = x1 + x2
            x1 = x2
            x2 = aux
            print(aux)
