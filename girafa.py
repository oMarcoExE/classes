from random import choice
class Girafa:

#Propriedades

#o método __init__ é executado quandos a calsse é instaciada

    def __init__(self, nome, altura, cor, idade, origem):
        self.nome = nome 
        self.altura = altura
        self.idade =  idade
        self.cor = cor
        self.origem = origem
        self.__fome = 100
    
    def andar(self):
        if self.__fome > 40:
            print(self.nome, "A girafa esta com fome, e não pode andar")
        else:
            print(self.nome, "A girafa esta andando")

    def comer(self, alimento):
        lista_alimentos = ['folhas', 'frutas', 'plantas']

        if alimento in lista_alimentos:
            self.__fome -= 10
        else:
            print(self.nome, "não come esse tipo de coisa...")

    def fome(self):
        if self.__fome > 60:
            print(self.nome, "Está morrendo de fome!")
        elif self.__fome > 40:
            print(self.nome, "esta com fome!")
        elif self.__fome > 20:
            print(self.nome, "está saciada.")
        elif self.__fome > 0:
            print(self.nome, "está cheia")
        elif self.__fome <= 0:
            print(self.nome, "está explodindo.")

    def respira(self):
        print(self.nome, "Inspira...")
        ##time.sleep(2)
        print(self.nome, "Expira")

    def reproduz(self, parceiro):
        if not isinstance(parceiro, Girafa):
            print(self.nome, "Sai correndo desesperado")

        nome = "Filhode de " + self.nome
        altura = (self.altura + parceiro.altura) / 2
        idade = 1
        cor = choice([self, parceiro]).cor
        origem = self.origem

        filhote = Girafa(nome, altura, idade, cor, origem)

        return filhote 