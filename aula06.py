#Listas criação e acesso aos dados
frutas = []

frutas = ["Laranja","Abacaxi","Uva"]

letras = list("python")

numeros = list(range(10))


#Para selecionar é só especificar 
# frutas[0]
# frutas[-1] pega o ultimo elemento 

lista = ["P","Y","T","H","O","N"]
lista[2:]
#t h o n
lista[:2]
#p y
lista[1:3]
#y t
lista[0:3:2]
#p t
lista[::]
#python
lista[::-1]
#nohtyp

lista.append("Python")
#adiciona um valor a lista

lista.clear()
#Limpa os valores de uma lista

lista.copy()
#muda o id da lista

lista.count()
#Conta quantos elementos tem na lista passando um valor

lista.extend()
#Adiciona tudo oq passar na lista

lista.index()
#Index informe a posição na lista 

lista.pop()
#pilha de pratos

lista.remove()
#Remove um elemento na lista

lista.reverse()
#coloca a lista ao contrario

lista.sort()
#Ordena a lista

