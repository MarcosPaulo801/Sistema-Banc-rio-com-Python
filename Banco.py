menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

  => '''

saldo = 0
limite = 500
extrato_depositos = []
extrato_saques = []
numero_saques = 0
LIMITE_SAQUES = 3 

while True:

    opcao = input(menu)

    if opcao == 'd':
       
        print('Deposito')
        print()
        valor = float(input('Valor: '))
        print()
        if valor > 0:
            saldo += valor
            extrato_depositos.append((valor))
            print(f'Deposito de R${valor:.2f} realizado com sucesso!')
            
        else:
            print('Quantidade invalida para depositar')  


    elif opcao == 's':
        print('Saque')
        print()
        #verifica se ele nao atingiu a quantidade maxima de saques no dia 
        if numero_saques < 3:
            valor = float(input("Valor: "))
            print()
            # verifica se o valor esta dentro do limite de saque e verifica se ele tem esse valor na conta para sacar 
            if valor <= limite and saldo > valor:
                print(f'Saque de {valor:.2f} foi realizado com sucesso!')
                saldo -= valor
                numero_saques += 1
                extrato_saques.append((valor))
            else:
                print('Valor nao permitido ou saldo insuficiente"')
        else:
            print('Voce nao pode mais sacar pois ultrapassou o limite diario')

    elif opcao == 'e':
        print("-Depositos-")
        if  not extrato_depositos :
            print("Sem movimentaçoes")
        for i in extrato_depositos:
            print(f"D: R${i:.2f}")
        print()

        print('-Saques-')
        if not extrato_saques:
            print('Sem movimentaçoes')
        for i in extrato_saques:
            print(f'S: R${i:.2f}')
        print('\n-----------------------------------------')
        print(f'Saldo final : R${saldo}')

        

    
    elif opcao == 'q':
        break

    else:
        print("Operaçao invalido , por favor digite uma opçao valdia ")