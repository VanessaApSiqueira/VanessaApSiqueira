#comando for é usado para percorrer um objeto interavel
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    print("Aprendendo estrutura de repetição em python!")

# Função Range  é usada para produzir uma sequência de numeros inteiros a partir de um inicio (inclusivo) para um fim (exclusivo)
# Range com for

for numero in range(0,11):
    print(numero, end=" ")

# Exibindo a tabuada  do 5

for numero in range(0, 51, 5):
    print(numero, end=" ")

# Comando while é usado para repetir um bloco de código varias vezes

opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar, [2] Extrato, \n [0] Sair: *"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# break
while True:
    numero = int(input("informe um numero: "))
    if numero == 10:
        break
    print(numero)