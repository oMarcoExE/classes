from classeCalculadora import Calculadora

nmr1 = int (input("Digite nmr1: "))
nmr2 = 0
operador = input("Digite um operador lógico: ")

calculadora = Calculadora(nmr1, nmr2)

if operador == '+':
    nmr2 = int (input("Digite nmr2: "))
    calculadora.verificacao(nmr1, nmr2)
    calculadora.adicao(nmr1, nmr2)

elif operador == '-':
    nmr2 = int (input("Digite nmr2: "))
    calculadora.verificacao(nmr1, nmr2)
    calculadora.subtracao(nmr1, nmr2)

elif operador == '*':
    nmr2 = int (input("Digite nmr2: "))
    calculadora.verificacao(nmr1, nmr2)
    calculadora.multiplicacao(nmr1, nmr2)

elif operador == '/':
    nmr2 = int (input("Digite nmr2: "))
    if nmr2 == 0 or nmr1 == 0:
        print("Não é possivel dividir por 0!")
    calculadora.verificacao(nmr1, nmr2)
    calculadora.divisao(nmr1, nmr2)

elif operador == '^':
    nmr2 = int (input("Digite nmr2: "))
    calculadora.verificacao(nmr1, nmr2)
    calculadora.potencia(nmr1, nmr2)
