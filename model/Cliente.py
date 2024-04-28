from Conta import Conta
from Transacao import Transacao

class Cliente:
    def __init__(self, endereco, contas:list[Conta]) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        pass

    def adicionar_conta(self, conta: Conta):
        pass