from abc import ABC, abstractmethod
from .conta_corrente import Conta_Corrente

class Transacao(ABC):
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta:Conta_Corrente):
        resultado = conta.despositar(self._valor)

        if resultado:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta:Conta_Corrente):
        resultado = conta.sacar(self._valor)

        if resultado:
            conta.historico.adicionar_transacao(self)