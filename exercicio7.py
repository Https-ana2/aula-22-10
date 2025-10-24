# 7. Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).

class Aluno:
    def __init__ (self, nome, nota):
        self.nome = nome
        self.nota = nota

    def resultado (self):
        if self.nota >= 7 :
            print(f'O aluno(a) {self.nome} tirou a nota: {self.nota}')
            print('Situação: Foi Aprovado(a)!!')
        elif self.nota >=6:
            print(f'O aluno(a) {self.nome} tirou a nota: {self.nota}')
            print('Situação: Está de Recuperação.')
        else:
            print(f'O aluno(a) {self.nome} tirou a nota: {self.nota}')
            print('Situação: Foi Reprovado(a)!!')
        
        print('----------------------------------')

aluno1 = Aluno ('Ana', 8)
aluno2 = Aluno ('Junior', 5)
aluno3 = Aluno ('Carlos', 6)
aluno4 = Aluno ('Mirela', 1)

aluno1.resultado()
aluno2.resultado()
aluno3.resultado()
aluno4.resultado()


