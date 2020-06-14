import random, os

baralho_inicial = ['Ás de Paus', '2 de Paus', '3 de Paus', '4 de Paus',
'5 de Paus', '6 de Paus', '7 de Paus', '8 de Paus', '9 de Paus',
'Valete de Paus', 'Dama de Paus', 'Rei de Paus','Ás de Ouros', '2 de Ouros', '3 de Ouros', '4 de Ouros',
'5 de Ouros', '6 de Ouros', '7 de Ouros', '8 de Ouros', '9 de Ouros',
'Valete de Ouros', 'Dama de Ouros', 'Rei de Ouros', 'Ás de Copas', '2 de Copas', '3 de Copas', '4 de Copas',
'5 de Copas', '6 de Copas', '7 de Copas', '8 de Copas', '9 de Copas',
'Valete de Copas', 'Dama de Copas', 'Rei de Copas', 'Ás de Espadas', '2 de Espadas', '3 de Espadas', '4 de Espadas',
'5 de Espadas', '6 de Espadas', '7 de Espadas', '8 de Espadas', '9 de Espadas',
'Valete de Espadas', 'Dama de Espadas', 'Rei de Espadas']

baralho_final = baralho_inicial[:]

random.shuffle(baralho_final)
tentativas = 0
print('Baralho Inicial:')
for c in baralho_inicial:
    print(c)
print('Baralho Final:')
for c in baralho_final:
    print(c)
contador = 100
while True:
    if baralho_final != baralho_inicial:
        random.shuffle(baralho_final)
        tentativas += 1
        contador -= 1
    else:
        break
    if contador == 0:
#        print('Baralho Final:')
#        for c in baralho_final:
#            print(c)
        print(f'Tentativa {tentativas} e ainda falha')
#        os.system('cls')
        contador = 10000
print('Baralho Final:')
for c in baralho_final:
    print(c)
print('Baralho Completamente organizado')
print(f'Tentativas: {tentativas}')
input()

