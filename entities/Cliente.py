from .transacao import Transacao
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
    
    def verificar_numero_conta(self,numero_conta):
        for conta in self._contas:
            if conta.numero == numero_conta:
                return True
        return False
    
    def selecionar_conta(self):
        print('\nDeseja ver o histórico de qual conta? (Digite o número da conta)')
        for conta in self._contas:
            print(f'{conta.numero} - Agência: {conta.agencia}, Saldo: R${conta.saldo:.2f}')

        numero_conta_input = input('\n- Numero da conta: ')

        if self.verificar_se_ha_letra(numero_conta_input) == None:
            return False
        else:
            numero_conta_input = int(numero_conta_input)

            if self.verificar_numero_conta(numero_conta_input):
                 return self.retornar_conta(numero_conta_input)
            else:
                return False

    @staticmethod
    def verificar_se_ha_letra(input_usuario:str): # Retorna o input recebido se só houver números na str, caso contrário, vai retornar None
        if input_usuario.isdigit():
            return input_usuario
        else:
            return None

# Classe filha:Pessoa Física
class Fisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome
    
    @property
    def endereco(self):
        return self._endereco
        
    @property
    def data_nasc(self):
        return self._data_nascimento
    
        