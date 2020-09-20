from random import randint
tentativas = 0
senha = ''
while True:
    tentativa = randint(1, 10000)
    ten = str(f'{tentativa:0>4}')
    if ten == senha:
        print(f'Sucesso com {tentativas} a senha e {ten}')
        break
    else:
        tentativas +=1
#        print(ten)
#        print(f'falha tentativa {tentativas}')
        continue
