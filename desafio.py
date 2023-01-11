menu = '''

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe um valor para depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito                                R$ {valor:.2f}\n'

        else :
            print('Operação não concluiu! O valor apresentado é invalido.')

    elif opcao == 's':
        valor = float(input('Informe um valor para saque: '))
        
        excedeu_valor = valor > saldo

        excede_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_valor:
            print('Operação não concluiu! Você não possui saldo suficiente.')
        
        elif excede_limite:
            print('Operação não concluiu! O valor excede o limite de saque.')

        elif excedeu_saques:
            print('Operação não concluiu! Você excedeu o limite de saques.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque                                   R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print('Operação não concluiu! O valor apresentado é invalido.')

    elif opcao == 'e':
        print('\n=============== Inicio do Extrato ===============')
        print('Não foi realizado movimentação na conta.' if not extrato else extrato)
        print(f'\nSaldo:                                  R$ {saldo:.2f}')
        print('=============== Final do Extrato ================')

    elif opcao == 'q':
        break

    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')