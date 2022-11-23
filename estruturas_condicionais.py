import sys

# Estrutura condicional simples composta por um unico desvio (if)

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:      # Se  saldo é maior ou igual a saque
    print("Realizando o saque!")
if saldo < saque:       # Se saldo é menor  que saque
    print("Saldo insuficiente!")
    # Em caso de retorno verdadeiro as ações presentes no bloco de código serão executados

    # Estrutura condicional com dois desvios  (if/ else)
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:  #Se  saldo é maior ou igual a saque
    print("Realizando o saque!")

else:               # Caso contrario
    print("Saldo insuficiente!")

    # Estrutura condicional com mais de dois desvio (elif)
opcao = int(input("Informe uma opção: [1] Sacar /n[2] Extrato:"))

if opcao == 1:
    valor = float(input("informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o Extrato...")

else:
    sys.exit("Opção invalida")

    # Estrutura condicional If aninhado
    # Para criar estrutura condicional aninhado basta adicionar if/elif/else  dentro do bloco de código de estrutura if/elif/else

conta_normal = True
conta_universitaria =False

saldo =2000
saque =200
cheque_especial =450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque < (saldo + cheque_especial):
        print("Saque realizado com o uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

        # If ternario
        # O If ternario permite escrever uma condição em uma unica linha

saldo = 2000
saque = 500

        # Composto por três partes 1º é o retorno caso a expressão retorne verdadeioro  2º parte é a expressão lógica 3º parte é o retorno caso a  expressão não seje atrendido

status= "Sucesso!" if saldo >= saque else "falha!"
print(f"{status} ao realizar o saque!")