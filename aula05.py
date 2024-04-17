# class ContaBancaria:
#    def __init__(self, titular, saldo=0):
#        self.titular = titular
#        self.saldo = saldo

#    def depositar(self, valor):
#        if valor > 0:
#            self.saldo += valor
#           print(f'Depósito de R${valor} realizado com sucesso.')
#       else:
#           print('O valor do depósito deve ser maior que zero.')

#    def sacar(self, valor):
#        if 0 < valor <= self.saldo:
#            self.saldo -= valor
#            print(f'Saque de R${valor} realizado com sucesso.')
#        else:
#            print('Saldo insuficiente para realizar o saque.')

#    def verificar_saldo(self):
#        print(f'Saldo atual: R${self.saldo}')


# Exemplo de uso:
#if __name__ == "__main__":
#    conta1 = ContaBancaria("João")
#    conta1.depositar(100)
#    conta1.verificar_saldo()
#    conta1.sacar(50)
#    conta1.verificar_saldo()
#

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor= float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou! O valor informado é invalido.")
    elif opcao == "s":
        valor= float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor> limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo o suficiente.")
        elif excedeu_limite:
            print("Operação falhou! Você não tem limite o suficiente.")
        elif excedeu_saques:
            print("Operação falhou! Você não tem saques o suficiente.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é invalido.")
    
    elif opcao =="e":
        print("==================== Extrato ========================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida. Por favor selecione a opção novamente")

