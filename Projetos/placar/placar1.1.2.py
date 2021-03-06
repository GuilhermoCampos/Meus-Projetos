# Manipulação do Arquivo


def abrir(path):
    """
    
    :param path: 
    :return: 
    """
    try:
        a = open(path, 'tr')
        return False
    except:
        print(f'{"Criando Arquivo...":^60}')
        a = open(path, 'w+')
        sleep(2)
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
    try:
        nome = str(input('Nome: ')).capitalize().strip()
        pont = 0
        gravar(arquivo, 'a', f'{nome};{pont}\n')
    except:
        print('Não foi possivel Adicionar')
    else:
        print(f'{nome} adicionado com sucesso')
        sleep(1)

def modificar(path, arquivo):
    if len(arquivo) == 0:
        print('Lista Vazia')
        sleep(1)
        return
    pos = leiaInt('Posição: ') - 1
    if pos >= len(arquivo) or pos < 0:
        print(f'"{pos+1}" É uma posição inválida')
        print('Por favor tente novamente')
        sleep(3)
        return
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
    else:
        print('Pontuação Adicionada com Sucesso!')


def removerpessoa(path, arquivo):
    if len(arquivo) == 0:
        print('Lista Vazia! Não é possivel remover!')
        input('Enter para continuar')
        return
    pos = leiaInt('Posição: ') - 1
    if -1 < pos <= len(arquivo):
        arquivo[pos] = arquivo[pos].split(';')
        deletado = arquivo[pos][0]
        while True:
            certeza = str(input(f'Tem Certeza que deseja Remover {deletado}? [S/N]: ')).strip().upper()[0]
            if certeza not in 'SN':
                print('Escolha Inválida')
                sleep(2)
            else:
                break
        if certeza == 'N':
            return
        del arquivo[pos]
        if len(arquivo) == 0:
                    f = open(path, 'w')
                    f.write('')
        else:
            try:
                for p , i in enumerate(arquivo): 
                    if len(arquivo) > 0:
                        i = i.split(';')
                        i[1] = i[1].replace('\n', '')
                        if p == 0:
                            f = open(path,'w')
                            f.write(f'{i[0]};{i[1]}\n')
                        else:
                            f = open(path, 'a')
                            f.write(f'{i[0]};{i[1]}\n')
            except Exception as erro:
                print(f'Falhao ao Remover da lista em arquivo: {erro.__class__}')
                input('Enter para continuar')
        f.close()
        print(f'{deletado} foi excluido da lista com sucesso!')
        sleep(2)
    else:
        print(f'"{pos+1}" Não faz parte da lista\nRetornando ao Menu Principal...')
        sleep(2)

def delarquivo(path):
    import os
    os.system(f'del {path}')
    pass


# Manipulação Da Interface


def linhas(inicio, fim , simb, tam):
    lin = simb * tam
    print(inicio, end='')
    print(f'{lin}', end='')
    print(fim)


def cabecalho(titulo):
    linhas('╔', '╗', '═', 58)
    print(f'║{titulo:^58}║')
    linhas('╠', '╣', '═', 58)

def menu(lista, ver=''):
    cabecalho('Menu Principal')
    for p, i in enumerate(lista):
        if i == lista[-1]:
            print(f'║ {p+1} - {i:<42}{ver:>10} ║')
        else:    
            print(f'║ {p+1} - {i:<53}║')
    linhas('╚', '╝', '═', 58)
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
    print(f'║ POS ║{"Nome":^40}║{"Pontuação":^11}║')
    linhas('╠', '╣', "═", 58)
    if len(arquivo) == 0:
        print(f'║{"":58}║')
        print(f'║{"Lista Vazia":^58}║')
        print(f'║{"":58}║')
    for p, c in enumerate(arquivo):
        print(f'║ {p+1:^3} ║ {c[0]:_<38} ║ {c[1]:>5} pts ║')
    linhas('╚', '╝', '═', 58)
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
clear()
cabecalho('Qual Tipo de Arquivo?')
print(f'║{"Padrão [1]":^28}║{"Personalizado [2]":^29}║')
linhas('╚','╝', '═', 58)
padrao = leiaInt('Escolha: ')
if padrao == 1:
    nome = 'placar.txt'
if padrao == 2:
    print('Não se esqueça do .txt no final')
    nome = str(input('Nome do arquivo: '))
abrir(nome)
while True:
    clear()
    opc = menu(['Ler Placar', 'Adicionar Pontuação', 'Adicionar Pessoa' , 'Remover Pessoa', 'Deletar Arquivo', 'Sair'], 'Ver. 1.1.2')
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
            input('Enter para continuar')
    elif opc == 3:
        try:    
            clear()
            mostrar(placar(ler(nome)))
            adicionar(nome)
            input('Enter para Continuar')
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
            print('DELETANDO!...')
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
