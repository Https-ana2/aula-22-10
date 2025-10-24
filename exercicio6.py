# 6. Crie uma classe Livro com título, autor e método exibir_detalhes().

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print(f'Livro: {self.titulo}')
        print(f'Autor: {self.autor}')
        print("-----------------------------")

livro1 = Livro('Harry Potter','J>K Rowling')
livro2 = Livro('Dom Casmurro','Machado de Assis')
livro3 = Livro('Moby Dick','Herman Melville')

livro1.exibir_detalhes()
livro2.exibir_detalhes()
livro3.exibir_detalhes()
