from codigo.bytebank import Funcionario

# gi = Funcionario('Giovana Ribeiro', '28/01/2007', 1400)
#
# print(gi.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2002', 111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/2001', 111)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/12/2001', 111)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()