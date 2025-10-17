from entities.pessoa_fisica import Fisica
from entities.conta_corrente import Conta_Corrente
from entities.transacao import Deposito, Saque
import re

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

def verificar_padrao_cpf(cpf):
    pattern = r'^\d{11}'
    if re.fullmatch(pattern, cpf):
        return True
    else:
        return False

# Funções do menu inicial

def menu_inicial():
    print(f'''
{' MENU '.center(30, '=')}

    [nu] - Novo usuário
    [eu] - Entrar no usuário
    [q] - Sair do programa

{''.center(30, '=')}''')
    
    return input('\n- Sua Escolha: ')

def novo_usuario(clientes):
    print()
    print(' Crindo Conta de Usuário '.center(30,'='))

    cpf = input('\nDigite seu CPF(Somente os números): ')

    if verificar_padrao_cpf(cpf):
        if verificar_cliente(cpf, clientes):
            print('\nJá existe um usuário com esse CPF no nosso sistema.')

        else:
            nome = input('Digite seu nome: ')
            endereco = input('Digite seu endereço: ')
            data_nasc = input('Digite sua data de nascimento(dd/mm/aaaa): ')

            print('\nConta criada com sucesso!')

            cliente = Fisica(endereco,cpf,nome,data_nasc)
            clientes.append(cliente)

    else:
        print('\nCPF informado é inválido.')
        
    print()
    print(''.center(30,'='))

# Funções do menu do usuário

def menu_usuario():
    print(f'''
{' MENU '.center(30, '=')}

    [o] - Operações da conta
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

    else:
        opcao_operacao = input('\nQual operação deseja realizar, depósito (d) ou saque (s)? ')

        match opcao_operacao:
            case 'd':
                print()
                print(' Depósito '.center(30,'='))

                # Passo 2: Criar instância de Depósito
                valor_deposito = float(input('\n- Qual é o valor do deposito?\nR$ '))
                deposito = Deposito(valor_deposito)

                # Passo 3: Realizar transação
                cliente_atual.realizar_transacao(conta_selecionada,deposito)

                print()
                print(''.center(30,'='))

            case 's':
                print()
                print(' Saque '.center(30,'='))

                # Passo 2: Criar instância de Saque
                valor_saque = float(input('\n- Qual é o valor do saque?\nR$ '))
                saque = Saque(valor_saque)

                # Passo 3: Realizar transição
                cliente_atual.realizar_transacao(conta_selecionada,saque)

                print()
                print(''.center(30,'='))

            case _:
                pass

def mostrar_historico(cliente_atual):
    print()
    print(f' Histórico da conta '.center(30,'='))

    # Passo 1: Escolher conta
    conta_selecionada = cliente_atual.selecionar_conta()

    if conta_selecionada == False:
        print(f'\nConta com o número informado não existe.')

    # Passo 2: Verificar se há um histórico
    else:
        if not conta_selecionada.historico.transacoes:
            print('\nOperações ainda não foram realizadas nessa conta.')

    # Passo 3: Mostrar o histórico da conta
        else:
            print()
            
            for transacao in conta_selecionada.historico.transacoes:
                print(f'{transacao['tipo']}: R${transacao['valor']} - {transacao['data']}')
            
            print(f'\nSaldo Atual: R${conta_selecionada.saldo}')

    print()
    print(''.center(30,'='))

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

def listar_contas_usuario(cliente_atual):
    print()
    print(' Contas vinculadas '.center(30,'='))

    if not cliente_atual.contas:
        print('\nVocê não tem contas vinculadas a esse usuário.')

    else:
        print()
        for conta in cliente_atual.contas:
            print(f'Conta {conta.numero} - Agência: {conta.agencia}, Saldo: R${conta.saldo:.2f}')

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
                            case 'o':
                                operacoes(cliente_atual)
                        # Mostrar Histórico do Usuário
                            case 'h':
                                mostrar_historico(cliente_atual)
                        #Criar Nova Conta
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