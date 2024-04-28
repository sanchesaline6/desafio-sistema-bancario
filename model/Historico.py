from Transacao import Transacao

class Historico:

    def __init__(self, transacoes: list[Transacao]) -> None:
        self.transacoes = transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)