# for pos, element in enumerate(my_set):

# desafio 72
# numeros_por_extenso = ('zero', 'um', 'dois', 'tres', 'quatro')

# numero_selecionado = int(input('Insira um numero de 0 a 4'))

# print(f'O numero selecionado foi {
# desafio 73
tabela_campeonato = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
                     'Flamengo', 'Athletico', 'Atletico', 'Fortaleza', 'Sao Paulo', 'America MG')
cinco_primeiros_colodados = tabela_campeonato[:5]
ultimos_quatro_colocados = tabela_campeonato[-4:]
ordem_alfabetica = sorted(tabela_campeonato)
posicao_fortaleza = tabela_campeonato.index('Fortaleza') + 1
print(cinco_primeiros_colodados)
print(ultimos_quatro_colocados)
print(ordem_alfabetica)
print(posicao_fortaleza)
