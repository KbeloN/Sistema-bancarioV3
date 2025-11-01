from entities.pessoa_fisica import Fisica
from entities.conta_corrente import Conta_Corrente
from entities.transacao import Deposito, Saque
from datetime import datetime
import re

# Classes utilitárias

class Conta_Iterador:
    def __init__(self, contas: list):
        self._contas = contas
        self._contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self._contas[self._contador]
            self._contador += 1
            return conta
        except IndexError:
            raise StopIteration
        
# Funções utilitarias

def verificar_cliente(cpf,clientes): # Retorna True se existe um usuário com o CPF recebido
    for cliente in clientes:
        if cliente.cpf == cpf:
            return True
    
    return False

def retornar_cliente_atual(cpf,clientes): # Pega o cliente que tem o mesmo CPF inserido e o retorna
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente

def log_transacao(func):
    def registro(*args, **kwargs):
        func(*args, **kwargs)
        print(f'\n{func.__name__.upper()} - {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')

    return registro

# Funções do menu inicial

def menu_inicial():
    print(f'''
{' MENU '.center(30, '=')}

    [nu] - Novo usuário
    [eu] - Entrar no usuário
    [q] - Sair do programa

{''.center(30, '=')}''')
    
    return input('\n- Sua Escolha: ')

@log_transacao
def novo_usuario(clientes):
    print()
    print(' Crindo Conta de Usuário '.center(30,'='))

    cpf = input('\nDigite seu CPF(Somente os números): ')

    nome = input('Digite seu nome: ')
    endereco = input('Digite seu endereço: ')
    data_nasc = input('Digite sua data de nascimento(dd/mm/aaaa): ')

    print('\nConta criada com sucesso!')

    cliente = Fisica(endereco,cpf,nome,data_nasc)
    clientes.append(cliente)

    print()
    print(''.center(30,'='))

# Funções do menu do usuário

def menu_usuario():
    print(f'''
{' MENU '.center(30, '=')}

    [op] - Operações da conta
    [h] - Histórico
    [nc] - Nova conta
    [lc] - Listar Contas
    [q] - Voltar ao menu inicial

{''.center(30, '=')}
''')
    
    return input('\n- Sua Escolha: ')

def operacoes(cliente_atual):
    # Passo 1: Escolher conta
    conta_selecionada = cliente_atual.selecionar_conta()

    if conta_selecionada == False:
        print(f'\nConta com o número informado não existe.')

    elif conta_selecionada == None:
        pass

    else:
        opcao_operacao = input('\nQual operação deseja realizar, depósito (d) ou saque (s)? ')

        # Passo 2: Escolher operação
        match opcao_operacao:
            case 'd':
                @log_transacao
                def deposito():
                    print()
                    print(' Depósito '.center(30,'='))

                    # Passo 2: Criar instância de Depósito
                    valor_deposito = float(input('\n- Qual é o valor do deposito?\nR$ '))
                    deposito = Deposito(valor_deposito)

                    # Passo 3: Realizar transação
                    cliente_atual.realizar_transacao(conta_selecionada,deposito)

                    print()
                    print(''.center(30,'='))
                deposito()

            case 's':
                @log_transacao
                def saque():
                    print()
                    print(' Saque '.center(30,'='))

                    # Passo 3: Criar instância de Saque
                    valor_saque = float(input('\n- Qual é o valor do saque?\nR$ '))
                    saque = Saque(valor_saque)

                    # Passo 4: Realizar transição
                    cliente_atual.realizar_transacao(conta_selecionada,saque)

                    print()
                    print(''.center(30,'='))
                saque()

            case _:
                print('\nValor inválido. Escolha d (Para deposito) ou s (Para saque).')

@log_transacao
def gerador_historico(cliente_atual):
    print()
    print(f' Histórico da conta '.center(30,'='))

    # Passo 1: Escolher Conta
    conta_selecionada = cliente_atual.selecionar_conta()

    if conta_selecionada == False:
        print(f'\nConta com o número informado não existe.')

    elif conta_selecionada == None:
        pass

    else:
        def print_transacao(tipo_transacao=None):
            if not conta_selecionada.historico.transacoes:
                print('\nOperações ainda não foram realizadas nessa conta.')

            else:
                print()
                for transacao in conta_selecionada.historico.gerar_historico(tipo_transacao):
                    print(f'{transacao['data']} - {transacao['tipo']}: R${transacao['valor']}')

                print(f'\nSaldo Atual: R${conta_selecionada.saldo}')


    # Passo 2: Escolher Tipo De Transação Para Filtrar
        filtro_transacao = input('\nQual transacao deseja visualizar, Saque (s), Depósito (d) ou Todas (t)? ')

        match filtro_transacao:
            case 's':
                print_transacao(Saque)
            case 'd':
                print_transacao(Deposito)
            case 't':
                print_transacao()
            case _:
                print('Valor inválido.')

    print()
    print(''.center(30,'='))

@log_transacao
def criar_nova_conta(cliente_atual):
    print()
    print(' Crindo Conta '.center(30,'='))

    numero_nova_conta = input('\n- Digite um número para essa conta: ')
    
    if Fisica.verificar_se_ha_letra(numero_nova_conta) == None:
        print('\nValor inválido.')

    else:
        numero_nova_conta = int(numero_nova_conta)

        if cliente_atual.verificar_numero_conta(numero_nova_conta):
            print('\nJá existe uma conta com esse número.')

        else:
            cliente_atual.adicionar_conta(Conta_Corrente.nova_conta(cliente_atual,numero_nova_conta))
    
    print()
    print(''.center(30,'='))

@log_transacao
def listar_contas_usuario(cliente_atual):
    print()
    print(' Contas vinculadas '.center(30,'='))

    if not cliente_atual.contas:
        print('\nVocê não tem contas vinculadas a esse usuário.')

    else:
        print()
        for conta in Conta_Iterador(cliente_atual.contas):
            print(conta)
            print()

    print(''.center(30,'='))

def main():
    clientes = []

    while True:
    # Menu inicial
        opcao_inicial = menu_inicial()

        match opcao_inicial:
        # Criar novo usuário
            case 'nu':
                novo_usuario(clientes)
        # Entrar no usuário    
            case 'eu':
                cpf_atual = input('\n- Seu CPF: ')

                if verificar_cliente(cpf_atual,clientes):

                    cliente_atual = retornar_cliente_atual(cpf_atual,clientes)
                    
                # Menu do usuário
                    while True:
                        opcao_usuario = menu_usuario()

                        match opcao_usuario:
                        # Depósito ou Saque
                            case 'op':
                                operacoes(cliente_atual)
                        # Mostrar Histórico do Usuário
                            case 'h':
                                gerador_historico(cliente_atual)
                        # Criar Nova Conta
                            case 'nc':
                                criar_nova_conta(cliente_atual)
                        # Listar Contas do Usuário
                            case 'lc':
                                listar_contas_usuario(cliente_atual)
                            case 'q':
                                break
                            case _:
                                print('Valor inválido.')
                else:
                    print('\nCliente não encontrado.')
        # Listar usuários
            case 'q':
                break
            case _:
                print('Valor inválido.')

main()