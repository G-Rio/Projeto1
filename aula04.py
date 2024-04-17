#Conhecendo metodos uteis da classe string
curso = "Python"

print(curso.upper())
# PYTHON   - Deixa tudo maiusculo 

print(curso.lower())
# python   - Deixa tudo minusculo 

print(curso.title())
# Python   - Deixa a primeira letra maiuscula 

print(curso.strip())
# "Python"  - Tira espaço em branco

print(curso.lstrip())
# "Python "   - Remove só espaço da esquerda

print(curso.rstrip())
# "   Python"   - Remove só espaco da direita

print(curso.center(10, "#"))
#  "##Python##"

print(".".join(curso))
#   "P.y.t.h.o.n"







#Interpolação de variaveis
# 3 formas %, format, f strings
nome = "Geovanne Almeida do Rio"
idade = 21
profissao = "programador"
linguagem = "python"

print("Ola me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))


print("Ola me chamo {3}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {0}." .format(idade, profissao, nome, linguagem))

print("Ola me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")











#Fatiamento de strings
nome[0]
# "G"

nome[:8]
# "Geovanne"

nome[9:]
# "Almeida do Rio"

nome[9:7]
# "Almeida"

nome[9:7:3]
# "Alm"

nome[:]
# "Geovanne Almeida do Rio"

nome[::-1]
# "oiR od adiemlA ennavoeG"





#String multiplas linhas


mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""