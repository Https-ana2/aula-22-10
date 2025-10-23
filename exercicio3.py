# 3. Crie uma classe Conta com saldo e métodos depositar() e sacar().

class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor 
        print(f'Saldo atual: {self.saldo}')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor     
        else:
            print('Saldo insuficiente.')
    
    def mostrarSaldo(self):
        print(f'Saldo atual: {self.saldo}')

    def dados (self):
        print(f'Olá, {self.cliente}')
              
cliente1 = Conta('Dona Odete', 700)

cliente1.dados()
cliente1.mostrarSaldo
cliente1.sacar(200)
cliente1.mostrarSaldo()
cliente1.depositar(790)
cliente1.depositar(54)
cliente1.mostrarSaldo()


    