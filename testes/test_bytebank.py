from codigo.bytebank import Funcionario
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








