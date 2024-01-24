from codigo.bytebank import Funcionario

# gi = Funcionario('Giovana Ribeiro', '28/01/2007', 1400)
#
# print(gi.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2002', 111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()