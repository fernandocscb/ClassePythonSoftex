
# Online Python - IDE, Editor, Compiler, Interpreter

'''Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.'''

class funcionario:
    cont=0
    def __init__(self, nome, idade, setor):
        self.nome=nome
        self.idade=idade
        self.setor=setor
        funcionario.cont+=1

    def muda_idade(self, nova_idade):
        self.idade=nova_idade

    def muda_setor(self, novo_setor):
        self.setor=novo_setor

funcionario1=funcionario("Joana", "42", "direção")
funcionario2=funcionario("Marcelo", "23", "marketing")
funcionario3=funcionario("José", "38", "RH")
funcionario2.muda_idade("24")
funcionario3.muda_setor("direção")
print(f'Funcionario: {funcionario1.nome}\nIdade: {funcionario1.idade}\nSetor: {funcionario1.setor}\n'
      f'Funcionario: {funcionario2.nome}\nIdade: {funcionario2.idade}\nSetor: {funcionario2.setor}\n'
      f'Funcionario: {funcionario3.nome}\nIdade: {funcionario3.idade}\nSetor: {funcionario3.setor}\n'
      f'Total de funcionarios cadastrados: {funcionario.cont}')