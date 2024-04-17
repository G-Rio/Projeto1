#Identação e blocos de comandos
#Em python a identação é extremamente importante pois não tem {} 
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('valor sacado')

sacar(100)


#Estruturas condicionais
# if, else, elif


#Estruturas de repetição
#for quando sabe quantas vezes vai ser executado
texto = input("informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print()

#while quando n sabe quantas vezes vai ser repetido
opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por utilizar o sistema...")
    