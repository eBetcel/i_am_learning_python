from pytest import mark
import pytest
from bytebank.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000' #Given - Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() #When - Ação

        assert resultado == esperado # Then - Desfecho

    def test_quando_o_nome_recebe_Lucas_Carvalho_deve_retornar_apenas_carvalho(self):
        entrada = 'Lucas Carvalho' #Given - Contexto
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)
        resultado = funcionario_teste.sobrenome() #When - Ação
        
        assert resultado == esperado # Then Desfecho

    @mark.calcular_bonus
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        entrada = 100000 #Given
        esperado = 90000

        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada)
        funcionario_teste.decrescimo_salario() #When

        resultado = funcionario_teste.salario
        
        assert esperado == resultado 

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado