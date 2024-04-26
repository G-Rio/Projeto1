import textwrap 

def menu():
    menu = """\n
    =============== MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tsair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: \tR$ {valor:.2f}\n"
        print("\n!!! Deposito realizado com sucesso! !!!")
    else:
        print("!!!  Operação falhou! O valor informado é invalido! !!!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Voê não tem saldo o suficiente ! @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! Voê não tem limite o suficiente ! @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Voê não tem saques o suficiente ! @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("!!! Saque realizado com sucesso! !!!")
    
    else:
        print("\n@@@  Operação falhou! O valor informado é invalido! @@@")

    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    print("\n ==================== EXTRATO ====================")
    print("nÃO FORAM REALIZADOS MOVIMENTAÇÕES." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n =================================================")


def criar_usuario(usuario):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereço = input("Informe o endereço: ")

    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("### Usuario criado com sucesso! ###")

def filtrar_usuario(cpf, usuario):
    usuario_filtrados = [usuario for usuario in usuario if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n### Conta criada com sucesso! ###")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do deposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo - saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="nu":
            criar_usuario(usuario)

        elif opcao =="nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação invalida, por favor selecione a operação desejada novamente")

main()