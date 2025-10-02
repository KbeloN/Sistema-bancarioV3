from .conta import Conta

class Conta_Corrente(Conta):
    def __init__(self, numero, agencia, cliente, historico):
        super().__init__(numero, agencia, cliente, historico)
        self._limite = 500.0
        self._limite_saques = 3