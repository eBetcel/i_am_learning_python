# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def eh_vogal(letra: str) -> bool:
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra in vogais:
        return True
    else:
        return False


# Faça um Programa que leia três números e mostre-os em ordem decrescente.
def ordena_desc(a, b, c) -> list:
    my_list = [a, b, c]
    my_list.sort(reverse=True)

    return my_list
