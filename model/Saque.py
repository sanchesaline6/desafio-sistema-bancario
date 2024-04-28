from Transacao import Transacao

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self.valor = valor