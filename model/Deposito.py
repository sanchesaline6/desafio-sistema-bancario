from .Transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self.valor = valor