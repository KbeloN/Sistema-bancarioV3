class Historico:
    def __init__(self):
        self._historico_conta = []

    def adicionar_transacao(self, transacao):
        self._historico_conta.append(transacao)

    def mostrar_historico(self,conta_selecionada):
        print()
        print(' Histórico '.center(30,'='))
        print()
        
        for transacao in self.historico_conta:
            print(f'{transacao.__class__.__name__} - R${transacao.valor:.2f}')

        print(f'\nSaldo atual: R${conta_selecionada.saldo:.2f}')

    @property
    def historico_conta(self):
        return self._historico_conta