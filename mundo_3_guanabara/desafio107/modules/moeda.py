def aumentar(valor, aumento, formato=False):
    res = valor + aumento
    return res if formato is False else formata_valor(res)

def diminuir(valor, diminuicao, formato=False):
    res =  valor - diminuicao
    return res if formato is False else formata_valor(res)
    

def dobro(valor, formato=False):
    res = valor * 2
    return res if formato is False else formata_valor(res)

def metade(valor, formato=False):
    res = valor / 2
    return res if formato is False else formata_valor(res)

def formata_valor(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2}'.replace('.',',')