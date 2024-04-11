import textwrap

def menu():
    menu = """
    ===================== MENU =====================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

saldo = 0.0
limite = 500
extratos = ""
numero_saques = 1
LIMITE_SAQUES = 3
depositos = 0
saques = 0


def deposito(valor):
    global saldo
    global depositos
    global extratos
    # Verificar se o valor informado é positivo
    if(valor > 0):
        saldo += valor
    else:
        print("Valor informado inválido. Por favor informar um valor positivo para depósito.")
    # Armazenar depósito em uma variável
    depositos += valor
    # Registrar a operação no extrato
    extratos += f"Depósito => R$ {valor:.f}\n"

def saque(valor):
     global saldo
     global extratos
     global saques
     global numero_saques

     
     # Verificar o limite de saque diário
     if(numero_saques <= LIMITE_SAQUES):
         if(valor <= 500): # Verificar se o valor do saque é inferior a R$ 500,00
             if(saldo >= valor):
                 saques += valor # Armazenar o saque em uma variável
                 saldo -= valor # Verificar se o usuário possui saldo em conta
                 numero_saques += 1
                 extratos += f"Depósito => R$ {valor:.f}\n" # Registrar a operação no extrato
             else:
                 print("Saldo insuficiente. Consulte seu saldo")
         else:             
            print("Valor do saque superior ao limite permitido.")
     else:
         print("Limite de saque diário ultrapassado.")      
    

def extrato():
    global saldo
    global extratos
    # Listar todas as operações realizadas
    if(extratos == ""):
        print("Nenhuma movimentação realizada até o momento")
    else:
        print(extratos)

    # Exibir o saldo atual da conta ao final do extrato
    print("Saldo: R$ " + '{:.2f}'.format(saldo)) # Utilizar o formato R$ xxx.xx para valores


while True:
    opcao = input(menu)

    match opcao:
        case "d":
            print("Opção escolhida: Depósito")
            valor = float(input("Informe o valor que deseja depositar: "))
            deposito(valor=valor)
        case "s":
            print("Opção escolhida: Saque")
            valor = float(input("Informe o valor que deseja sacar: "))
            saque(valor=valor)
        case "e":
            print("Opção escolhida: Extrato")
            extrato()
        case "q":
            print("Opção escolhida: Sair")
            break;
        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

