# Manipulação do Arquivo


def abrir(path):
    try:
        a = open(path, 'tr')
    except:
        print('Criando Arquivo...')
        a = open(path, 'w+')
    finally:
        a.close()


def ler(path):
    try:
        f = open(path, 'tr')
        arquivo = f.readlines()
        f.close()
        abriu = True
    except:
        abriu = False
    if abriu:    
        return arquivo
    else:
        print('Não foi possivel ler o arquivo')
        sleep(1)


def gravar(path, wra, gravacao):
    try:
        f = open(path, wra)
        abriu = True
    except Exception as erro:
        print(f'Não foi possivel devido erro: "{erro.__class__}"')
    if abriu:
        f.write(gravacao)
        f.close()


def adicionar(arquivo):
    nome = str(input('Nome: '))
    pont = 0
    gravar(arquivo, 'a', f'{nome};{pont}\n')


def modificar(path, arquivo):
    if len(arquivo) == 0:
        print('Lista Vazia')
        sleep(1)
        return
    pos = leiaInt('Posição: ') - 1
    pnt = leiaInt('Pontuação: ')
    try:    
        for p, i in enumerate(arquivo):
            i = i.split(';')
            i[1] = i[1].replace('\n', '')            
            if p == pos:
                i[1] = int(i[1])
                i[1] += pnt
            if p == 0:
                f = open(path, 'w')
                f.write(f'{i[0]};{i[1]}\n')
            else:
                f = open(path, 'a')
                f.write(f'{i[0]};{i[1]}\n')
        f.close()
    except Exception as erro:
        print(f'Falha ao Gravar lista em arquivo: {erro.__class__}')


def removerpessoa(path, arquivo):
    pos = leiaInt('Posição: ') - 1
    try:
        for p , i in enumerate(arquivo):
            i = i.split(';')
            i[1] = i[1].replace('\n', '')
            if p == pos and len(arquivo) > 1:
                f = open(path, 'a')
                del i
                f.write(f'')
                f.close()
                '''
                del i
                for p ,i in enumerate(arquivo):
                    if p == 0:
                        f = open(path, 'w')
                        f.write(f'{i[0]};{i[1]}\n')
                    else:
                        f.open(path, 'a')
                        f.write(f'{i[0]};{i[1]}\n')
                f.close()    
                return
                '''
            if p == 0 and p != pos:
                f = open(path, 'w')
                f.write(f'{i[0]};{i[1]}\n')
            elif pos == 0 and p == 1:
                f = open(path, 'w')
                f.write(f'{i[0]};{i[1]}\n')
            elif len(arquivo) == 1:
                f = open(path, 'w')
                f.write('')
                f.close()
                return
            else:
                f = open(path, 'a')
                f.write(f'{i[0]};{i[1]}\n')
        f.close()
    except Exception as erro:
        print(f'Falhao ao Remover da lista em arquivo: {erro.__class__}')
        input('Enter para continuar')
            

def delarquivo(path):
    import os
    os.system(f'del {path}')
    pass


# Manipulação Da Interface


def linhas(simb, tam):
    lin = simb * tam
    print(f'{lin}')


def cabecalho(titulo):
    linhas('=', 60)
    print(f'|{titulo:^58}|')
    linhas('=', 60)


def menu(lista):
    cabecalho('Menu Principal')
    for p, i in enumerate(lista):
        print(f'| {p+1} - {i:<53}|')
    linhas('=', 60)
    opc = leiaInt('Escolha uma Opção: ')
    return opc


def placar(arquivo):
    lista = list()
    pessoa = list()
    for linha in arquivo:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        lista.append(dado[:])
    return lista


def mostrar(arquivo):
    cabecalho('Placar')
    print(f'| {"Nome":^27}||{"Pontuação":^27} |')
    linhas("=", 60)
    for p, c in enumerate(arquivo):
        print(f'| {p+1:>3} - {c[0]:<22}{c[1]:>24} pts |')
    linhas('=', 60)
    pass


# Funções extras


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except:
            print('Por favor insira um número inteiro válido')
            continue
        else:
            return num
        

def clear():
    import os
    os.system('cls')


# Programa Principal
from time import sleep
padrao = leiaInt('Arquivo Padrão[1] ou Personalizado[2]?: ')
if padrao == 1:
    nome = 'placar.txt'
if padrao == 2:
    print('Não se esqueça do .txt no final')
    nome = str(input('Nome do arquivo: '))
abrir(nome)
while True:
    clear()
    opc = menu(['Ler Placar', 'Adicionar Pontuação', 'Adicionar Pessoa' , 'Remover Pessoa', 'Deletar Arquivo', 'Sair'])
    if opc == 1:
        try:
            clear()
            mostrar(placar(ler(nome)))
            input('Enter pra Continuar')
        except:
            print('Não foi possivel Ler o Placar!')
    elif opc == 2:
        try:    
            clear()
            mostrar(placar(ler(nome)))
            modificar(nome, ler(nome))
        except:
            print('Não Foi possivel Adicionar Pontuação!')
            sleep(3)
        else:
            input('Adicionado com Sucesso\nEnter para continuar')
    elif opc == 3:
        try:    
            clear()
            mostrar(placar(ler(nome)))
            adicionar(nome)
        except:
            print('Não foi possivel Adicionar Pessoa')
    elif opc == 4:
        try:
            clear()
            mostrar(placar(ler(nome)))
            removerpessoa(nome, ler(nome))
        except Exception as erro:
            print(f'Não Foi possivel remover: {erro.__class__} ')
    elif opc == 5:
        print('Deletando Arquivo, O programa irá fechar!')
        while True:
            try:
                certeza = str(input('Você tem certeza? [S/N]: ')).strip().upper()[0]
                if certeza not in 'SN':
                    print('Escolha Inválida, Por favor escolha entre Sim[S] e Não[N]!')
                    sleep(2)
                    clear()
                    continue
                else:
                    break
            except:
                print('Escolha Inválida!')
        if certeza == 'S':
            print('DELETADO!')
            sleep(2)
            delarquivo(nome)
            break
        else:
            continue
    elif opc == 6:
        print('Saindo do Programa')
        sleep(1)
        print('Até Logo...')
        sleep(1)
        break
    else:
        print('Opção Inválida')
        sleep(2)
        continue
'''
#print(opc)
abrir('test.txt')
#gravar('test.txt', 'a', 'Guilherme;13\n') 
#adicionar('test.txt')
arquivo = ler('test.txt')
#clear()
mostrar(placar(arquivo))
input()
modificar('test.txt', arquivo)
input()
'''
