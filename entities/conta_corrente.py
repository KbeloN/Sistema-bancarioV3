from .conta import Conta

class Conta_Corrente(Conta):
    def __init__(self, numero,cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        from .transacao import Saque

        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )
        
        if numero_saques >= self._limite_saques:
            print('\nConta Chegou ao Limite De Saques Diários')

        elif valor > self._limite:
            print('\nValor Inserido Excede o Limite De Saque Da Conta')

        else:
            return super().sacar(valor)
        
        return False
