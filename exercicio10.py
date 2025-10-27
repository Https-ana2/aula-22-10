# 10. Crie uma classe Retangulo com base e altura e método area().

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

retangulo = Retangulo(5, 10)

print(f"A área do retângulo é: {retangulo.area()}")