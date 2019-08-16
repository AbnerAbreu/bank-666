print('Bem-vindo ao Banco-666')

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
saldo = float(input('digite seu saldo: '))

print('\n digite(1) para saque \n digite(2) para depósito \n digite(3) para empréstimo \n digite(4) para visualizar informações \n digite (qualquer outro caracter) para sair')
operação = int(input('digite o numero da operação: '))

if(operação == 1):
    saque()

elif(operação == 2):
    deposito()

elif(operação == 3):
    emprestimo()


def saque(saque1):
    valorsaque = float(input('digite o valor do saque: '))
    if valorsaque > 1000 and saldo < valorsaque:
        print('impossivel efetuar saque')
    else:
        print('transição realizada com sucesso')
        print(saldo - valorsaque)

def deposito(deposito2):
    valordeposito = float(input('digite o valor do deposito: '))
    if valordeposito > 5000:
        print('impossivel efetuar deposito')
    else:
        print(valordeposito + saldo)

def emprestimo(emprestimoss):
    valoremprestimo = float(input('Digite o valor do Emprestimo: '))
    if valoremprestimo >= 2000 or valoremprestimo <= 15 * saldo:
        print(valoremprestimo + saldo)
    else:
        print('Emprestimo recusado')


saque()
deposito()
emprestimo()
