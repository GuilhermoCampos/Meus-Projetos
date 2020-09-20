""" Jogo da velha """
from time import sleep, asctime
from os import system
from random import randint, randrange


class Main():
    def __init__(self):
        self.nome = ''
        self.score1 = 0
        self.score2 = 0
        self.mode = ''
        self.player1 = ''
        self.player2 = ''
    def modo(self, modo):
        if modo == 1:
            self.mode = 'PVM'
        if modo == 2:
            self.mode = 'PVP'
    def player(self, opc):
        char = ''
        if opc == 1:
            char = 'X'
        elif opc == 2:
            char = 'O'
        self.player1 = char
        if self.player1 == 'X':
            self.player2 = 'O'
        elif self.player1 == 'O':
            self.player2 = 'X'
    def nomear(self, nome):
        self.nome = nome
    def win(self, score):
        self.score += score
    def salvar(self):
        try:
            open('score.txt', 'r+')
        except:
            open('score.txt', 'w+')
        try:
            date = asctime()
            save = open('score.txt', 'a')
            save.write(f'Nome={self.nome}\nScore={self.score}\nData={date}\n\n')
        except:
            print('falha')
class Tela():
    def __init__(self):
        self._1x1 = ' '
        self._1x2 = ' '
        self._1x3 = ' '
        self._2x1 = ' '
        self._2x2 = ' '      
        self._2x3 = ' '
        self._3x1 = ' '
        self._3x2 = ' '
        self._3x3 = ' '
    def clear(self):
        system('cls')
    def changePos(self, pos, marc):
        if pos == 1:
            if self._1x1 in "XO":
                return False
            else:
                self._1x1 = marc
                return True
        if pos == 2:
            if self._1x2 in "XO":
                return False
            else:
                self._1x2 = marc
                return True
        if pos == 3:
            if self._1x3 in "XO":
                return False
            else:
                self._1x3 = marc
                return True
        if pos == 4:
            if self._2x1 in "XO":
                return False
            else:
                self._2x1 = marc
                return True
        if pos == 5:
            if self._2x2 in "XO":
                return False
            else:
                self._2x2 = marc
                return True
        if pos == 6:
            if self._2x3 in "XO":
                return False
            else:
                self._2x3 = marc
                return True
        if pos == 7:
            if self._3x1 in "XO":
                return False
            else:
                self._3x1 = marc
                return True
        if pos == 8:
            if self._3x2 in "XO":
                return False
            else:
                self._3x2 = marc
                return True
        if pos == 9:
            if self._3x3 in "XO":
                return False
            else:
                self._3x3 = marc
                return True
    def checkEnd(self):
        end = False
        win = ''
        if self._1x1 == self._2x2 == self._3x3 == 'O':
            end = True
            win = 'O'
        elif self._1x1 == self._1x2 == self._1x3 == 'O':
            end = True
            win = 'O'
        elif self._1x1 == self._2x1 == self._3x1 == 'O':
            end = True
            win = 'O'
        elif self._2x1 == self._2x2 == self._2x3 == 'O':
            end = True
            win = 'O'
        elif self._1x2 == self._2x2 == self._3x2 == 'O':
            end = True
            win = 'O'
        elif self._1x3 == self._2x3 == self._3x3 == 'O':
            end = True
            win = 'O'
        elif self._3x1 == self._2x2 == self._1x3 == 'O':
            end = True
            win = 'O'
        elif self._3x1 == self._3x2 == self._3x3 == 'O':
            end = True
            win = 'O'
        elif self._1x1 == self._2x2 == self._3x3 == 'X':
            end = True
            win = 'X'
        elif self._1x1 == self._1x2 == self._1x3 == 'X':
            end = True
            win = 'X'
        elif self._1x1 == self._2x1 == self._3x1 == 'X':
            end = True
            win = 'X'
        elif self._2x1 == self._2x2 == self._2x3 == 'X':
            end = True
            win = 'X'
        elif self._1x2 == self._2x2 == self._3x2 == 'X':
            end = True
            win = 'X'
        elif self._1x3 == self._2x3 == self._3x3 == 'X':
            end = True
            win = 'X'
        elif self._3x1 == self._2x2 == self._1x3 == 'X':
            end = True
            win = 'X'
        elif self._3x1 == self._3x2 == self._3x3 == 'X':
            end = True
            win = 'X'
        if end:
            print('Win')
        return end, win

    def bot(self, cont):
        print(cont)
        if cont == 1:
            jog = randrange(1, 9, 2)
            return jog
            '''
            if self._1x1 in 'XO':
                jog = randint(0, 3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
            elif self._1x2 in 'XO':
                jog = randint(0, 4)
                if jog == 0:
                    return 1
                if jog == 1:
                    return 3
                if jog == 2:
                    return 7
                if jog == 3:
                    return 9
            elif self._1x3 in 'XO':
                jog = randint(0, 3)
                if jog == 0:
                    return 1
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
            elif self._2x1 in 'XO':
                jog = randint(0, 4)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
                if jog == 3:
                    return 1
            elif self._2x2 in 'XO':
                jog = randint(0, 4)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
                if jog == 3:
                    return 1
            elif self._2x3 in 'XO':
                jog = randint(0, 4)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
                if jog == 3:
                    return 1
            elif self._3x1 in 'XO':
                jog = randint(0, 3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 1
                if jog == 2:
                    return 9
            elif self._3x2 in 'XO':
                jog = randint(0, 4)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 9
                if jog == 3:
                    return 1
            elif self._3x3 in 'XO':
                jog = randint(0, 3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 7
                if jog == 2:
                    return 1
            else:
                return 'False'
            '''
        elif cont == 3:
            if self._1x1 == self._1x3 == iniciar.player1:
                return 2
            elif self._1x1 == self._3x1 == iniciar.player1:
                return 4
            elif self._1x1 == self._3x3 == iniciar.player1:
                return 5
            elif self._2x1 == self._2x3 == iniciar.player1:
                return 5
            elif self._1x2 == self._3x2 == iniciar.player1:
                return 5
            elif self._3x1 == self._3x3 == iniciar.player1:
                return 8
            elif self._3x1 == self._1x3 == iniciar.player1:
                return 5
            elif self._1x3 == self._3x3 == iniciar.player1:
                return 6
            elif self._1x1 == self._1x2 == iniciar.player1:
                return 3
            elif self._1x1 == self._2x2 == iniciar.player1:
                return 9
            elif self._1x1 == self._2x1 == iniciar.player1:
                return 7
            elif self._1x2 == self._2x2 == iniciar.player1:
                return 8
            elif self._1x3 == self._2x3 == iniciar.player1:
                return 9
            elif self._2x1 == self._2x2 == iniciar.player1:
                return 6
            elif self._2x2 == self._2x3 == iniciar.player1:
                return 4
            elif self._3x1 == self._3x2 == iniciar.player1:
                return 9
            elif self._3x2 == self._3x3 == iniciar.player1:
                return 7
            elif self._3x1 == self._2x2 == iniciar.player1:
                return 3
            elif self._3x3 == self._2x2 == iniciar.player1:
                return 1
            elif self._3x1 == self._2x1 == iniciar.player1:
                return 1
            elif self._3x2 == self._2x2 == iniciar.player1:
                return 2
            elif self._3x3 == self._2x3 == inicuar.player1:
                return 3
            elif self._1x1 == iniciar.player2:
                jog = randint(0,3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 9
                if jog == 2:
                    return 7
            elif self._1x3 == iniciar.player2:
                jog = randint(0,3)
                if jog == 0:
                    return 1
                if jog == 1:
                    return 9
                if jog == 2:
                    return 7
            elif self._3x1 == iniciar.player2:
                jog = randint(0,3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 9
                if jog == 2:
                    return 1
            elif self._3x3 == iniciar.player2:
                jog = randint(0,3)
                if jog == 0:
                    return 3
                if jog == 1:
                    return 1
                if jog == 2:
                    return 7
            else:
                return 'Fail'
        elif cont == 5:
            pass
        elif cont == 7:
            pass

    def screen(self):
        self.clear()
        print('╔', end='')
        print('═'*3, end='')
        print('╦', end='')
        print('═'*3, end='')
        print('╦', end='')
        print('═'*3, end='')
        print('╗')
        print('║', end='')
        print(f' {self._1x1} ', end='')
        print('║', end='')
        print(f' {self._1x2} ', end='')
        print('║', end='')
        print(f' {self._1x3} ', end='')
        print('║')
        print('╠', end='')
        print('═'*3, end='')
        print('╬', end='')
        print('═'*3, end='')
        print('╬', end='')
        print('═'*3, end='')
        print('╣')
        print('║', end='')
        print(f' {self._2x1} ', end='')
        print('║', end='')
        print(f' {self._2x2} ', end='')
        print('║', end='')
        print(f' {self._2x3} ', end='')
        print('║')
        print('╠', end='')
        print('═'*3, end='')
        print('╬', end='')
        print('═'*3, end='')
        print('╬', end='')
        print('═'*3, end='')
        print('╣')
        print('║', end='')
        print(f' {self._3x1} ', end='')
        print('║', end='')
        print(f' {self._3x2} ', end='')
        print('║', end='')
        print(f' {self._3x3} ', end='')
        print('║')
        print('╚', end='')
        print('═'*3, end='')
        print('╩', end='')
        print('═'*3, end='')
        print('╩', end='')
        print('═'*3, end='')
        print('╝')

# Programa

iniciar = Main()
print('╔', end='')
print('═'*30, end='')
print('╗')
print('║', end='')
print(f'{"Jogo Da Velha":^30}', end='')
print('║')
print('╚', end='')
print('═'*30, end='')
print('╝')
modo = int(input('Singleplayer[1] ou Multiplayer[2]: '))
iniciar.modo(modo)
opc = int(input('Jogador 1 escolhe X[1] ou O[2]?: '))
iniciar.player(opc)
teste = Tela()
teste.screen()
cont = 0
end = False
while end == False:
    print(cont)
    livre = False
    while livre == False:
        pos = int(input(f'Jogador 1 "{iniciar.player1}" pos: '))
        livre = teste.changePos(pos, iniciar.player1)
    teste.screen()
    check = teste.checkEnd()
    end = check[0]
    win = check[1]
    if end == True:
        break
    cont += 1
    if cont == 9:
        win = 'Empate'
        break
    if iniciar.mode == "PVP":
        livre = False
        while livre == False:
            pos = int(input(f'Jogador 2 "{iniciar.player2}" pos: '))
            livre = teste.changePos(pos, iniciar.player2)
    if iniciar.mode == "PVM":
        livre = False
        while livre == False:
            pos = teste.bot(cont)
            print(f'Computador escolhe: {pos}')
            livre = teste.changePos(pos, iniciar.player2)
    teste.screen()
    check = teste.checkEnd()
    end = check[0]
    win = check[1]
    cont += 1
print(win)
input()
'''
teste.changePos(1, '♣')
teste.changePos(2, '♠')
teste.changePos(3, '♥')
teste.changePos(4, '♦')
teste.changePos(5, '0')
teste.changePos(6, 'O')
teste.changePos(7, 'X')
teste.changePos(8, '●')
teste.changePos(9, '□')
teste.screen()
teste.__init__()
teste.screen()
teste.checkEnd()
'''
#nome = str(input('Nome: '))
#iniciar.nomear(nome)
#iniciar.win(2)
#iniciar.salvar()



