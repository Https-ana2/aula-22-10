# 4. Crie uma classe Animal com método falar().

class Animal:
    def __init__(self, animal, tipoSom, som):
        self.animal = animal
        self.som = som
        self.tipoSom = tipoSom
    
    def falar(self):
        print(f'Os {self.animal} se comunicam através de {self.tipoSom}, Que soam assim "{self.som}"')

animal1 = Animal('Gatos', 'miados', 'Miau')
animal2 = Animal('Cachorros', 'latidos', 'Au Au')

animal1.falar()
animal2.falar()