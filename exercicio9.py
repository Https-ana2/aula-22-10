# 9. Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}"

class Gerente(Funcionario):

    def __init__(self, nome, salario, setor):

        super().__init__(nome, salario)
        self.setor = setor

    def __str__(self):
        return f"Gerente: {self.nome}, Salário: R${self.salario:.2f}, Setor: {self.setor}"

funcionario = Funcionario("Ana", 3000)
gerente = Gerente("Carlos", 5000, "Vendas")

print(funcionario)
print(gerente)     