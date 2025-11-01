from .conta import Conta

class Conta_Corrente(Conta):
    def __init__(self, numero,cliente, limite=500):
        super().__init__(numero, cliente)
        self._limite = limite

    def sacar(self, valor):

        if self.historico.saques_do_dia() >= 3:
            print('\n@@@ Você chegou ao limite diário de saques! @@@')

        elif valor > self._limite:
            print('\nValor Inserido Excede o Limite De Saque Da Conta')

        else:
            return super().sacar(valor)
        
        return False
