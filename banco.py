contas = {}

def criar_conta():
    numero_conta = input("Digite o número da conta: ")
    nome_cliente = input("Digite o nome do cliente: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    contas[numero_conta] = {'nome': nome_cliente, 'saldo': saldo_inicial}
    print("Conta criada com sucesso.")

def verificar_saldo():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        print("Saldo atual da conta de {}: R$ {:.2f}".format(contas[numero_conta]['nome'], contas[numero_conta]['saldo']))
    else:
        print("Conta não encontrada.")

def depositar():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor a depositar: "))
        contas[numero_conta]['saldo'] += valor
        print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
        print("Novo saldo da conta de {}: R$ {:.2f}".format(contas[numero_conta]['nome'], contas[numero_conta]['saldo']))
    else:
        print("Conta não encontrada.")

def sacar():
    numero_conta = input("Digite o número da conta: ")
    if numero_conta in contas:
        valor = float(input("Digite o valor a sacar: "))
        if valor <= contas[numero_conta]['saldo']:
            contas[numero_conta]['saldo'] -= valor
            print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            print("Novo saldo da conta de {}: R$ {:.2f}".format(contas[numero_conta]['nome'], contas[numero_conta]['saldo']))
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Conta não encontrada.")

def encerrar_atendimento():
    print("Encerrando atendimento. Obrigado por utilizar nossos serviços.")

def menu():
    print("\n=== Menu ===")
    print("1. Criar conta")
    print("2. Verificar saldo")
    print("3. Depositar dinheiro")
    print("4. Sacar dinheiro")
    print("5. Encerrar atendimento")

    opcao = input("Escolha uma opção: ")
    return opcao

while True:
    opcao = menu()

    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        verificar_saldo()
    elif opcao == '3':
        depositar()
    elif opcao == '4':
        sacar()
    elif opcao == '5':
        encerrar_atendimento()
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
