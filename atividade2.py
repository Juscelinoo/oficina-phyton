print ("Hello World")

#Digitar um numero e imprimir na tela
numero = input("Digite um numero: ")
print ("O numero digitado foi: ", numero)

#Calcular a médiad de 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print ("A média é:", round(media, 2))

#Multiplicação de dois numeros inteiros e soma com um numero real

nint1 = int(input("Digite um numero inteiro: "))
nint2 = int(input("Digite outro numero inteiro: "))
nreal1 = float(input("Digite um numero real: "))

R1 = (2 * nint1 * nint2 / 2)
print ("O resultado é: ", R1)

R2 = (3 * nint1 + nreal1)
print ("O resultado é: ", R2)

R3 = (nreal1 ** 3)
print ("O resultado é: ", R3)

#Verifica se o numero é negativo ou positivo

n = int(input("Digite um numero: "))
if n < 0:
    print ("O numero é negativo")
elif n > 0:
    print ("O numero é positivo")
else :
    print ("O numero é zero")

#Verifica de o numero é maior ou igual

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
if n1 > n2:
    print ("O primeiro numero é maior")
elif n1 < n2:
    print ("O segundo numero é maior")
else:
    print ("Os numeros são iguais")

    #Verifica o sexo

f = ("Feminino")
m = ("Masculino")
sexo =input("Digite o sexo (f/m): ")
if sexo == "f":
    print ("Feminino")
elif sexo == "m":
    print ("Masculino")
else:

    print ("Sexo invalido")

    # Solicita as duas notas parciais do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Verifica o status do aluno com base na média
if media >= 7:
    print(f"A média é {media:.2f}. Aluno aprovado!")
elif media < 5:
    print(f"A média é {media:.2f}. Aluno reprovado!")
else: 
    print(f"A média é {media:.2f}. Aluno em recuperação!")

#Colocar valor entre 0 e 10 para ser valido
while True:
    nota = float (input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print ("Nota valida")
        break
    else:
        print ("Nota invalida, digite novamente")

# Solicita o nome de usuário e senha
# e verifica se a senha é igual ao nome de usuário

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha == usuario:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    else:
        print("Usuário e senha cadastrados com sucesso!")
        break

 # População inicial e taxas de crescimento
populacao_a = 80000
populacao_b = 200000
taxa_a = 0.03  # 3%
taxa_b = 0.015  # 1.5%

anos = 0

# Calcula o número de anos necessários
while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1

# Exibe o resultado
print("Serão necessários {anos} anos para que a população do país A ultrapasse ou iguale a população do país B.")   

#imprimir numeros de 1 a 20
for i in range(1, 20):
    print (i + 1) 

    # Imprime números ímpares de 1 a 50
for i in range(1, 50):
    if i + 1 % 2 != 0:  # Verifica se o número é ímpar
        print(i)

        # Imprime os primeiros 20 números em ordem decrescente
for i in range(20, 0, -1):
    print(i)

    # Inicializa as variáveis para armazenar as somas
soma_pares = 0
soma_impares = 0

# Itera pelos números de 500 a 800 (inclusive)
for i in range(500, 801):
    if i % 2 == 0:  # Verifica se o número é par
        soma_pares += i
    else:  # Caso contrário, é ímpar
        soma_impares += i

# Exibe os resultados
print(f"A soma dos números pares entre 500 e 800 é: {soma_pares}")
print(f"A soma dos números ímpares entre 500 e 800 é: {soma_impares}")