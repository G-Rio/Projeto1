#Conjuntos

#SETS elimina valores duplicados mas não garante a ordem

set([1,2,3,1,3,4])

set("abacaxi")

#CONJUNTOSSSSS
#UNIÃO
conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}


#INTERSEÇÃO
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.intersection(conjunto_b) # {2,3}

#DIFERENÇA

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

#DIFERENÇA SIMETRICA


conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

conjunto_a.symmetric_difference(conjunto_b) # {1,4}

#CONJUNTO DE OUTRO

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5,6,7,8}

conjunto_a.issubset(conjunto_b) #TRUE
conjunto_b.issubset(conjunto_a) #False


#CONJUNTO DE OUTRO AO CONTRARIO

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5,6,7,8}

conjunto_a.issuperset(conjunto_b) #False
conjunto_b.issuperset(conjunto_a) #True

#DESJUNTO 

conjunto_a = {1,2,3,4,5}
conjunto_b = {6,7,8,9}
conjunto_c = {1,0}

conjunto_a.isdisjoint(conjunto_b)#True
conjunto_a.isdisjoint(conjunto_c)#False

#ADD

sorteio = {1,23}

sorteio.add(25) # {1,23,25}
sorteio.add(42) # {1,23,25,42}
sorteio.add(25) # {1,23,25,42}

#CLEAR

sorteio = {1,23}

sorteio.clear()

#COPY
#FAZ UMA CÓPIA

#DISCARD
#DESCARTA MSM SE N TIVER O VALOR


#POP
#DESCARTA O ITEM COM INDICE DEFINIDO

#REMOVE
#DA ERRO SE N TIVER O VALOR PRA REMOVER

#LEN 
#MOSTRA TAMANHO

#IN
#MOSTRA SE O VALOR TEM NA LISTA