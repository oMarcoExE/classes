from girafa import Girafa

girafa = Girafa("Melman", 4.15, "Amarela e Marrom", 32, "Africa Central")
girafa2 = Girafa("Gepeto", 5.15, "Amarela e verde", 29, "Africa Central")

print(girafa.nome)
girafa2.comer('folhas')
girafa2.comer('folhas')
girafa2.comer('folhas')
girafa2.comer('folhas')

girafa2.fome()
girafa2.andar()
girafa.respira()

girafa2.reproduz(girafa)



