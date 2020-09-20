senha = '8592'
for c in range(1,10000):
    if f'{c:>4}' == senha:
        print(f'Sucesso a senha e {c}')
        break
#    else:
#        print(f'Falha tentativa {c}')
    
