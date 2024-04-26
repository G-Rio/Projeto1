#Funções -----------------------------------------------------------------------------------------
#Função é um bloco de código que tem um nome o indentificador eu posso enviar parametros para ela, ela pode retornar valores
#
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome = "Geovanne"):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "Anonimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome = "Geovanne")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Larissa")


#RETORNANDO VALORES--------------------------------------------------------------------------------

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

calcular_total([10,20,34])
retorna_antecessor_sucessor(10)