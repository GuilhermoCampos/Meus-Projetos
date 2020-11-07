"""
def trans(hora):
    minuto = hora * 60
    segundo = minuto * 60
    return minuto, segundo
    
    
def volta(segundos):
    minutos = segundos // 60
    hora = minutos // 60
    return minutos, hora
"""

def horaSegundo(hora):
    segundos = hora * (60**2)
    return segundos
    
    
def minutoSegundo(minuto):
    segundos = minuto * 60
    return segundos


def segundoHora(segundos):
    hora = segundos // (60**2)
    return hora
    
    
def segundoMinuto(segundos):
    minuto = (segundos % (60**2)) // 60
    return minuto


def relogio(rel):
    if rel[0] == '0':
        hora = int(rel[1])
    else:
        hora = int(rel[1]) + 10
    minuto = int(rel[3:5])
    return hora, minuto


while True:
    opc = int(input('opção: '))
    if opc == 0:
        break
    if opc == 1:
        hora = int(input('Hora: '))
        conv = trans(hora)
        print(f'A hora {hora}, são {conv[0]} minutos e {conv[1]} segundos')
    if opc == 2:
        segundos = int(input('Segundos: '))
        conv = volta(segundos)
        print(f'Os segundos {segundos}, em minutos são {conv[0]}, em horas são {conv[1]}')
    if opc == 3:
        rel = str(input('Relogio: '))
        relo = relogio(rel)
        print(relo)
        min1 = horaSegundo(relo[0])
        min2 = minutoSegundo(relo[1])
        print(f'A hora {rel} convertida em segundos é {min1+min2}')
    if opc == 4:
        diferenca = 0
        data1 = str(input('Primeira data: ')), str(input('Hora: '))
        data2 = str(input('Segunda data: ')), str(input('Hora: '))
        if int(data1[0][0:2]) < int(data2[0][0:2]):
            diferenca = int(data2[0][0:2]) - int(data1[0][0:2])
            hora1 = horaSegundo(int(data1[1][0:2])) + minutoSegundo(int(data1[1][3:5]))
            hora1 = horaSegundo(24) - hora1 
            if diferenca > 1:
                hora1+= horaSegundo(24) * (diferenca-1)
        if int(data1[0][0:2]) == int(data2[0][0:2]):
            hora1 = horaSegundo(int(data1[1][0:2])) + minutoSegundo(int(data1[1][3:5]))
        hora2 = horaSegundo(int(data2[1][:2])) + minutoSegundo(int(data2[1][3:5]))
        hora3 = hora1 + hora2
        print(f'{segundoHora(hora3)}:{segundoMinuto(hora3)}')
        print(f'a diferenca de dias é: {diferenca} dias')           
