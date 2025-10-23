# 1. Crie uma classe Pessoa com os atributos nome e idade.
# Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

pessoa1 = Pessoa('Ana', '17')
pessoa2 = Pessoa('Ricardo', '40')
pessoa1.saudacao()
pessoa2.saudacao()