menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

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
        saldo = saldo + valor
    else:
        print("Valor informado inválido. Por favor informar um valor positivo para depósito.")
    # Armazenar depósito em uma variável
    depositos = depositos + valor
    # Registrar a operação no extrato
    extratos = extratos + "Depósito => R$ " + '{:.2f}'.format(valor) + "\n"

def saque(valor):
     global saldo
     global extratos
     global saques
     global numero_saques

     
     # Verificar o limite de saque diário
     if(numero_saques <= LIMITE_SAQUES):
         if(valor <= 500): # Verificar se o valor do saque é inferior a R$ 500,00
             if(saldo >= valor):
                 saques = saques + valor # Armazenar o saque em uma variável
                 saldo = saldo - valor # Verificar se o usuário possui saldo em conta
                 numero_saques = numero_saques + 1
                 extratos = extratos + "Saque => R$ " + '{:.2f}'.format(valor) + "\n" # Registrar a operação no extrato
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

    if opcao == "d":
        print("Opção escolhida: Depósito")
        valor = float(input("Informe o valor que deseja depositar: "))
        deposito(valor)
    elif opcao == "s":
        print("Opção escolhida: Saque")
        valor = float(input("Informe o valor que deseja sacar: "))
        saque(valor)
    elif opcao == "e":
        print("Opção escolhida: Extrato")
        extrato()
    elif opcao == "q":
        print("Opção escolhida: Sair")
        break;
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

