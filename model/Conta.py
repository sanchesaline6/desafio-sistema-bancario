from Cliente import Cliente
from Historico import Historico

class Conta():
    def __init__(self, saldo, numero, agencia, cliente: Cliente, historico: Historico) -> None:
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
    
    def saldo(self):
        pass

    def nova_conta(self, cliente: Cliente, numero):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass