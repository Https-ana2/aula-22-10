# 5. Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def mostrarPreco(self):
        print(f'O preço do(a) {self.nome} é de R$:{self.preco}')
    
    def descontos(self): 
        desconto = float(self.preco * 0.10)
        desconto = self.desconto
        print(f'Foi feito um desconto de 10%. (R$: {desconto})')

    def mostrarRecibo(self):
        precoNovo = self.preco - desconto
        print(f'O produto {self.nome} custava R$:{self.preco}, Porém, ele teve um desconto de 10% (R$:{desconto}), O preço atual é {precoNovo}.')

Produto1 = Produto ('Vestido', '700')

Produto1.mostrarPreco()
Produto1.descontos()
Produto1.mostrarRecibo()