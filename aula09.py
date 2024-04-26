#DICIONARIOS
pessoa = {"nome": "Geovanne", "idade":21}          # Cria dicionario

pessoa = dict(nome="Geovanne", idade= 21)          # Cria dicionario

pessoa["telefone"] = "994113016"                   #Adiciona parametro e valor   

pessoa["nome"]                                     #Mostra valor do parametro

pessoa["nome"] = "Larissa"                         #Sobescreve o valor 


contatos = {
    "geovanne1542rio@gmail.com": {"nome":"Geovanne", "Telefone":"994113016"},
    "geovannaAlmeido@gmail.com": {"nome":"Geovanna", "Telefone":"994113017"},
    "geovannerio@gmail.com": {"nome":"Gervasio", "Telefone":"994113018"},
    "g1542rio@gmail.com": {"nome":"Setembrino", "Telefone":"994113019"},
}

telefone = contatos["geovanne1542rio@gmail.com"]["telefone"]
print(telefone)


for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

#METODOS DE CLASSE DICT
contatos = {
    "geovanne1542rio@gmail.com": {"nome":"Geovanne", "Telefone":"994113016"},
    "geovannaAlmeido@gmail.com": {"nome":"Geovanna", "Telefone":"994113017"},
    "geovannerio@gmail.com": {"nome":"Gervasio", "Telefone":"994113018"},
    "g1542rio@gmail.com": {"nome":"Setembrino", "Telefone":"994113019"},
}

#clear

#copy

#fromkeys cria chaves mas n passa valor

#get segunda forma de acessar valores

#items 

#keys retorna só as chaves

#pop remove um valor

#popitem retira itens na sequencia 

#setdefaut se n tiver ele adiciona no dicionario mas se tiver ele mostra o valor

#update atualiza um dicionario com outro dicionario

#values retorna só os valores

#in verifica em boleano 