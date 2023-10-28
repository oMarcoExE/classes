
class Calculadora:
    
    def __init__(self, nmr1, nmr2):
        self.nmr1 = nmr1
        self.nmr2 = nmr2

    def adicao(self, nmr1, nmr2):
        
        print("Resultado = ", nmr1 + nmr2)

    def subtracao(self, nmr1, nmr2):
        print("Resultado = ", nmr1 - nmr2)

    def multiplicacao(self, nmr1, nmr2):
        print("Resultado = ", nmr1 * nmr2)
    
    def divisao(self, nmr1, nmr2):
       print("Resultado = ", nmr1 / nmr2)
    
    def potencia(self, nmr1, nmr2):
        print("Resultado = ", nmr1**nmr2)

    def verificacao(self, nmr1, nmr2):
        if not isinstance(nmr1, (int, float)):
            print("Numnero um não é valido")

        if not isinstance(nmr2, (int, float)):
            print("Numero dois não é valido")
