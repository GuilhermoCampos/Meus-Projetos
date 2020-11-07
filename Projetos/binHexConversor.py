def DecToBin():
    while 1:
        bi = ''
        decimal = True
        dec = str(input('Decimal Number: '))
        inicial = dec
        try:
            dec = int(dec)
        except:
            print('Insira um número decimal inteiro válido')
        else:
            break
    binInicial = 65536
    while 1:
        if (dec - binInicial) >= 0:
            bi += '1'
            dec -= (binInicial)
        else:
            bi += '0'
        binInicial //= 2
        if binInicial == 0:
            break
    for c in range(0, len(bi)):
        if bi[c] == '1':
            first = c
            break
    bi = bi[c:]
    return inicial, bi


def DecToHex():
    hexa = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
            9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    while 1:
        hx = ''
        decimal = True
        dec = str(input('Decimal Number: '))
        inicial = dec
        try:
            dec = int(dec)
        except:
            print('Inira um número decimal inteiro válido')
        else:
            break
#    hexInicial = 4294967295
    while 1:
        if dec == 0:
            break
        else:
            hx += hexa[dec%16]
            dec //= 16
    hx = hx[::-1]
    return inicial, hx


def BinToDec():
    while 1:
        dec = 0
        binario = True
        bi = str(input('Binary Number: '))
        for c in range(0, (len(bi))):
            if bi[c] != '0' and bi[c] != '1':
                binario = False
        if binario is True:
            break
        else:
            print('O número binário foi inserido de forma errada, digite apenas 0 e 1')
    multi = 2**(len(bi)-1)
    for c in range(0, (len(bi))):
        if bi[c] == '1':
            dec += multi
        multi //= 2
    return bi, dec


def HexToDec():
    hexa = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
            '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    dec = 0
    
    hx = str(input('Hexadecimal Number: ')).lower().strip()
    multi = 16**(len(hx)-1)
    for c in hx:
        num = hexa[c]
        dec += num * multi
        multi //= 16
    return hx, dec


while 1:
    opc = str(input('Dec to Bin (1), Dec to Hex (2), Bin to Dec (3) or Hex to dec (4): '))
    if opc == '1':
        opc1 = DecToBin()
        print(f'Dec: {opc1[0]} \nBin: {opc1[1]}')
    if opc == '2':
        opc2 = DecToHex()
        print(f'Dec: {opc2[0]} \nHex: {opc2[1]}')
    if opc == '3':
        opc3 = BinToDec()
        print(f'Bin: {opc3[0]} \nDec: {opc3[1]}')
    if opc == '4':
        opc4 = HexToDec()
        print(f'Hec: {opc4[0]} \nDec: {opc4[1]}')
    if opc == '5':
        break
    else:
        continue

print(1)
