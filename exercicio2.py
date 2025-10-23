# 2. Crie uma classe Carro que tenha modelo, ano e velocidade.
# Adicione métodos acelerar() e frear().

class Carro:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor 
        self.velocidade = 0 
    
    def acelerar(self):
        self.velocidade += 20
        print(f'{self.nome} está a {self.velocidade} km/h')

    def frear(self):
        self.velocidade -= 20
        print(f'{self.nome} reduziu para {self.velocidade} km/h')

carro1 = Carro('Uno', 'Branco')
carro2 = Carro('Porshe', 'Amarela')
carro1.acelerar()
carro1.acelerar()
carro2.acelerar()
carro1.frear()
carro2.frear()  
