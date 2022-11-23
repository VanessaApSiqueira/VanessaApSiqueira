curso = "  PyThoN  "

print(curso.upper()) # converte todos os caracteres para maiusculo.

print(curso.lower()) # Converte todos os caracteres para minusculo.

print(curso.title()) # Converte apenas a primeira letra para maiusculo.

print(curso.strip()) # Remove espaço em branco.

print(curso.lstrip()) # Remove espaço em branco da esquerda (left strip).

print(curso.rstrip()) # Remove espaço em branco  da direita (right strip).

print(curso.center(10, "#")) # Centraliza a variavel e completa com a quantidade  de caracteres informado como parametro.

print(".".join(curso)) # Passa de item em item fazendo a junção colocando o caractere informado.

# Old style %

nome = "Vanessa Siqueira"
idade = 32
profissao = "Programadora"
linguagem = "Python"

print("Olá, me chamo %s. eu tenho %d anos de idade, trabalho como %s, e estou matriculada no curso de %s." % (nome, idade, profissao, linguagem))

# Método pouquissimo usado  %s= string  %d= int.

#método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {}, e estou matriculada no curso de {}.".format(nome, idade, profissao, linguagem))

# existem outras formas de usar o método format
# Ex: Pasando o indice das variaveis dentro das chaves {2}...{3}...{0}...
# Passando o nome da variavel dentro das chaves {nome}... {idade}... .format(nome=nome...)
# Passando o nome da variavel dentro das chaves {nome}...  .format(**pessoas)

# Método f-string

print(f"Olá, me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissao}, e estou matriculada no curso de {linguagem}.")

# Formatar strings com f-string

pi = 3.14159
print(f"Valor de pi: {pi: .2f}")
print(f"Valor de pi: {pi: 10.2f}")

# Fatiamento de strings

nome = "Vanessa Siqueira"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[8:16])
print(nome[8:16:2])
print(nome[:])
print(nome[: : -1])
print(nome[-1])
print(nome[-2])

# String de multiplas linhas/ strings triplas

nome = "Vanessa"

mensagem = f""" Olá, meu nome é {nome}...
Eu estou aprendendo
PYTHON!!!
######### @@@ #########
"""
print(mensagem)