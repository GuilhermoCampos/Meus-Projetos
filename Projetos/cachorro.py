class Cachorro():
    def __init__(self):
        self.nome = str(input('Nome do Cachorro: '))
        self.raca = str(input('Raça: '))
        self.idade = int(input('Idade: '))
        self.cor = str(input('Cor: '))
        self.passeando = False
        self.comendo = False
        self.lavando = False
    
    def passear(self):
        if self.passeando:
            self.passeando = False
            print(f'{self.nome} Parou de passear')
        else:
            self.passeando = True
            print(f'Passeando com {self.nome}')

    def comer(self):
        if self.comendo:
            self.comendo = False
            print(f'{self.nome} Parou de comer')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo')

    def lavar(self):
        if self.lavando:
            self.lavando = False
            print(f'{self.nome} Parou de se lavar')
        else:
            self.lavando = True
            print(f'{self.nome} está tomando banho')


dog1 = Cachorro()

while True:
    opc = int(input('Opção: '))
    if opc == 1:
        dog1.passear()
    elif opc == 2:
        dog1.comer()
    elif opc == 3:
        dog1.lavar()
    elif opc == 4:
        break
    else:
        continue
