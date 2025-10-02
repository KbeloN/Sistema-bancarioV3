from abc import ABC,abstractmethod
from .conta import Conta

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self,conta:Conta):
        resultado = conta.despositar(self._valor)

        if resultado:
            conta.historico.adicionar_transacao(self)
            print('\nOperação de deposito foi realizada!')
        else:
            print('\nOperação de deposito não foi realizada!')



class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        resultado = conta.sacar(self._valor)

        if resultado:
            conta.historico.adicionar_transacao(self)
            print('\nOperação de saque foi realizada!')
        else:
            print('\nOperação de saque não foi realizada!')
