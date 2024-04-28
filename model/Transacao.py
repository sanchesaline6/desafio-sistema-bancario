from abc import ABC, abstractmethod
from Conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta: Conta):
        pass