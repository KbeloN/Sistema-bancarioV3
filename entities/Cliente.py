from .transacao import Transacao,Saque
from abc import ABC

class Cliente(ABC):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(self, conta, transacao:Transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
        print('\nConta adicionada!')

    def retornar_conta(self, numero_conta):
        for conta in self._contas:
            if conta.numero == numero_conta:
                return conta
            
        return False
    
    def verificar_numero_conta(self, numero_conta):
        for conta in self._contas:
            if conta.numero == numero_conta:
                return conta
            
        return False
    
    def selecionar_conta(self):
        if not self._contas:
            print('\nVocê não tem contas vinculadas a esse usuário.')
            return

        else:
            print('\nQual Conta Deseja Selecionar? (Digite o número da conta)')

            for conta in self._contas:
                print(f'{conta.numero} - Agência: {conta.agencia}, Saldo: R${conta.saldo:.2f}')

            numero_conta_input = input('\n- Numero da conta: ')

            if self.verificar_se_ha_letra(numero_conta_input) != None:
                numero_conta_input = int(numero_conta_input)
                return self.retornar_conta(numero_conta_input)
                
        return False

    @staticmethod
    def verificar_se_ha_letra(input_usuario:str): # Retorna o input recebido se só houver números na str, caso contrário, vai retornar None
        if input_usuario.isdigit():
            return input_usuario
        else:
            return None