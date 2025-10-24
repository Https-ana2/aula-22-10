# 9. Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.

class Funcionario:
    def _init_(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def _str_(self):
        return f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}"


class Gerente(Funcionario):
    def _init_(self, nome, salario, setor):
        super()._init_(nome, salario)
        self.setor = setor

    def _str_(self):
        return f"Gerente: {self.nome}, Salário: R${self.salario:.2f}, Setor: {self.setor}"

