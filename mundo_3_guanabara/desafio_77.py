def extrai_vogais(palavras):
    vogais = ('a', 'e', 'i', 'o', 'u')
    for palavra in palavras:
        print(f'{palavra}: ', end='')
        for letra in palavra:
            if letra in vogais:
                print(letra, end=' ')
        print('')


minhas_palavras = 'carro','elefante','morango','ovo'

extrai_vogais(minhas_palavras)