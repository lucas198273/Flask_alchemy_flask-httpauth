class Calculadora:

    def __init__(self,adicao,subtracao):
        self.adicao = adicao
        self.subtracao = subtracao
    def add(self,num1,num2,op):
        if op:
            return self.adicao.soma(num1,num2)
        return None

    def sub(self,num1,num2,op):
        if op:
            return self.subtracao.diferenca(num1,num2)
        return None