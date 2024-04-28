from .Conta import Conta
from .Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self.valor = valor

    def registrar(self, conta: Conta):
        return super().registrar(conta)
    
    