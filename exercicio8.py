# 8. Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2 

    def somar(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero."
        return self.num1 / self.num2
    


calc1 = Calculadora(8, 9)         
calc2 = Calculadora(14, 3) 
calc3 = Calculadora(12, 7) 
calc4 = Calculadora(25, 5)                                                                                                                                     

calc1.somar()
calc2.subtrair()
calc3.multiplicar()
calc4.dividir()