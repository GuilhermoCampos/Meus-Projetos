from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Jãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
