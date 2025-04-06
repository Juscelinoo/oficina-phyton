def soma ():
    x = float(input("Primeiro numero:" ))
    y = float(input("Segundo numero:"  ))

    print ("soma: ", x + y )
def subtração ():
    x = float(input("Primeiro numero:" ))
    y = float(input("Segundo numero:"  ))
    print ("subtração: ", x - y)

def multiplicação ():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print ("multiplicação: ", x * y)

def divisão ():
        x = float(input("Primeiro numero: "))
        y = float(input("Segundo numero: "))
        print ("divisão: ", x / y)

opcao=1


while opcao:
    print ("0, sair")
    print ("1, soma")
    print ("2, subtração")
    print ("3, multiplicação")
    print ("4, divisão")
    
    opcao = int(input("opcao: "))
    if (opcao == 0):
        break
    elif (opcao == 1):
        soma()
    elif (opcao == 2):
        subtração()
    elif (opcao == 3):
        multiplicação()
    elif (opcao == 4):
        divisão()

    