from abc import ABC
from .historico import Historico

class Conta(ABC):

    def __init__(self,numero,cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)
    
    def __str__(self):
        return f"""Titular: {self.cliente.nome}
C/C: {self.numero}
Agência: {self.agencia}
Saldo atual: R${self.saldo:.2f}"""
    
    def sacar(self,valor):
        if valor > self.saldo:
            print('\n@@@ Saldo Insuficiente Para Continuar a Operação. @@@')

        elif valor > 0:
            self._saldo -= valor
            print('\n== Saque Feito Com Sucesso! ==')
            return True
        
        else:
            print('@@@ Operação Falhou. O Valor Inserido é Inválido @@@')
            
        return False

    def despositar(self,valor):
        if valor <= 0:
            print('\n@@@ Valor Inserido é Menor Que o Mínimo Esperado. @@@')

        else:
            self._saldo += valor
            print('\n= Deposito Feito Com Sucesso! =')
            return True

        return False