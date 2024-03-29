
from codigo.bytebank import Funcionario
import pytest
from pytest import mark
class TestClass:
    def test_quando_idade_recebe_13_03_2002_deve_retornar_22(self):
        entrada = '13/03/2002' # Given(contexto)
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When(ação)

        assert resultado == esperado # Then(desfecho)
    def test_quando_sobrenome_recebe_Giovana_Ribeiro_da_Silva_deve_retornar_Sliva(self):
        entrada = 'Giovana Ribeiro da Silva'  # Given(contexto)
        esperado = 'Silva'

        giovana = Funcionario(entrada, '28/01/2007', 1800)
        resultado = giovana.sobrenome() # When(ação)

        assert resultado == esperado # Then(desfecho)

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000  # Given(contexto)
        entrada_nome = 'Giovana Silva'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '03/03/1974',  entrada)
        funcionario_teste.decrescimo_salario() # When(ação)
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then(desfecho)


    @mark.calcular_bonus # pytest -v -m calcular_bonus(no terminal)
    def test_quando_calcular_bonus_recebe_1000_recebe_100(self):
        entrada = 1000 # Given(contexto)
        esperado = 100

        funcionario = Funcionario('Gica','28/01/2006', entrada)
        resultado = funcionario.calcular_bonus() # When(ação)

        assert resultado == esperado # Then(desfecho)
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000  # Given(contexto)

            funcionario = Funcionario('Gica', '28/01/2006', entrada)
            resultado = funcionario.calcular_bonus()  # When(ação)

            assert resultado # Then(desfecho)




# pytest -k idade
# pytest -v -k idade
# pytest --cov=codigo testes/ --cov-report term-missing
# pytest --cov=codigo testes/ --cov-report html (cria o relatório)


