# Manipulação do Arquivo


def abrir(path):
    """
    Tenta abrir o arquivo no caminho que recebe. Caso não encontre o arquivo,
    Cria um arquivo com o nome no caminho especificado.
    :param path: Local onde o arquivo está ou será criado.
    """
    try:
        a = open(path, 'tr')
        return False
    except:
        a = open(path, 'w+')
        c = 0
        while c < 57:
            clear()
            if c < 56:
                cabecalho('Criando Arquivo...')
            else:
                cabecalho('Arquivo Criado!')
            cheio = "■" * c
            vazio = "□" * (56 - c)
            print(f'║ {cheio}{vazio} ║', flush=True)
            linhas('╚', '╝', '═', 60, flush=True)
            c += 1
            sleep(0.01)
        input('Enter para Continuar')
    finally:
        a.close()


def ler(path):
    """
    Abre um arquivo no caminho especificado e adiciona o conteudo em uma lista separada pelas linhas do arquivo.
    :param path: Local do arquivo a ser lido.
    """
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
    """
    Abre um arquivo no caminho especificado. Do modo que lhe é definido e adiciona informações a esse arquivo.
    :param path: Local do arquivo onde as informações serão adicionadas.
    :param wra: Modo em que o arquivo será aberto. Sendo: 'r' - leitura, 'w' - escrita, 'a' - adicionar.
    :param gravacao: Conteudo que será salvo no arquivo.
    """
    try:
        f = open(path, wra)
        abriu = True
    except Exception as erro:
        print(f'Não foi possivel devido erro: "{erro.__class__}"')
    if abriu:
        f.write(gravacao)
        f.close()


def adicionar(path):
    """
    Adiciona novos participantes a tabela.
    :param path: Local do arquivo em que o participante será adicionado. 
    """
    try:
        nome = str(input('Nome: ')).title().strip()
        pont = 0
        nome = nome[0:38]
        gravar(path, 'a', f'{nome};{pont}\n')
    except:
        print('Não foi possivel Adicionar')
    else:
        print(f'{nome} adicionado com sucesso')
        sleep(1)

def modificar(path, arquivo):
    """
    Apenas modifica um elemento dentro do arquivo.
    :param path: Local do arquivo a ser modificado.
    :param arquivo: Lista de informações que serão modificadas e gravadas no arquivo.
    """
    if len(arquivo) == 0:
        print('Lista Vazia')
        sleep(1)
        return
    pos = leiaInt('Posição: ') - 1
    if pos >= len(arquivo) or pos < 0:
        print(f'"{pos+1}" É uma posição inválida')
        print('Por favor tente novamente')
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
    """
    Remove um participante de uma tabela.
    :param path: Local do arquivo a ser modificado.
    :param arquivo: Lista de informações que serão modificadas e gravadas no arquivo.
    """
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
    """
    Deleta o arquivo do local especificado.
    :param path: Local do arquivo a ser deletado.
    """
    import os
    os.system(f'del {path}')
    c = 0
    while c < 57:
        clear()
        if c < 56:
            cabecalho('Deletando Arquivo...')
        else:
            cabecalho('Arquivo Deletado!')
        cheio = "■" * (56 - c)
        vazio = "□" * c
        print(f'║ {cheio}{vazio} ║', flush=True)
        linhas('╚', '╝', '═', 60, flush=True)
        c += 1
        sleep(0.01)
    input('Enter para Continuar!')


# Manipulação Da Interface


def linhas(inicio, fim , simb, tam, end='\n', flush=False):
    """
    Cria uma sequência de simbolos formando uma linha
    :param inicio: Caractere que será utilizado na primeira posição da linha.
    :param fim: Caractere que será utilizado na última posição da linha.
    :param simb: Simbolo que será utilizado em todo o restante da linha.
    :param tam: Tamanho total que a linha terá.
    :param end: Função que define como a linha irá terminar. O padrão é '\n' para que 
    o proximo print seja feito uma linha abaixo.
    :param flush: Define se a atualização do print será constante.
    """
    lin = simb * (tam - 2)
    print(inicio, end='')
    print(f'{lin}', end='')
    print(fim)


def cabecalho(titulo):
    """
    Cria um cabeçalho padrão com um titulo personalizavel.
    :param titulo: Titulo do cabeçalho.
    """
    linhas('╔', '╗', '═', 60)
    print(f'║{titulo:^58}║')
    linhas('╠', '╣', '═', 60)

def menu(lista, ver=''):
    """
    Cria um menu com todas as opções que forem adicionadas a lista.
    :param lista: Lista com todas as opções que serão mostradas no menu.
    :param ver: Versão atual do programa que será exibido no canto inferior direito do menu.
    """
    cabecalho('Menu Principal')
    for p, i in enumerate(lista):
        if i == lista[-1]:
            print(f'║ {p+1} - {i:<42}{ver:>10} ║')
        else:    
            print(f'║ {p+1} - {i:<53}║')
    linhas('╚', '╝', '═', 60)
    opc = leiaInt('Escolha uma Opção: ')
    return opc


def organizar(arquivo):
    """
    Organiza os itens de um arquivo em uma lista.
    :param arquivo: Arquivo a ser organizado em uma lista.
    """
    lista = list()
    for linha in arquivo:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        lista.append(dado[:])
    return lista


def mostrar(lista):
    """
    Mostra uma lista organizada dos participantes. Com a Posição, O Nome e a Pontuação atual do participante.
    :param lista: Lista que será mostrada.
    """
    cabecalho('Placar')
    print(f'║ POS ║{"Nome":^40}║{"Pontuação":^11}║')
    linhas('╠', '╣', "═", 60)
    if len(lista) == 0:
        print(f'║{"":58}║')
        print(f'║{"Lista Vazia":^58}║')
        print(f'║{"":58}║')
    for p, c in enumerate(lista):
        print(f'║ {p+1:^3} ║ {c[0]:_<38} ║ {c[1]:>5} pts ║')
    linhas('╚', '╝', '═', 60)
    pass


# Funções extras


def leiaInt(txt):
    """
    Aceitando apenas que o usuário adicione um valor inteiro, caso não seja inserido um valor inteiro,
    é soliciado novamente que o Usuário digite um número que não está na lista o menu é recarregado adicione um valor inteiro.
    :param txt: Texto a ser exibido solicitando os dados do Usuário digite um número que não está na lista o menu é recarregado.
    """
    while True:
        try:
            num = int(input(txt))
        except:
            print('Por favor insira um número inteiro válido')
            continue
        else:
            return num
        

def clear():
    """
    Limpa o prompt de comando.
    """
    import os
    os.system('cls')


# Programa Principal
from time import sleep
clear()
# */ Pergunta o Usuário digite um número que não está na lista o menu é recarregado se o arquivo a ser aberto será o arquivo padrão 'placar.txt' 
# ou um arquivo com nome personalizado. /* 
while True:
    cabecalho('Qual Tipo de Arquivo?')
    print(f'║{"Padrão [1]":^28}║{"Personalizado [2]":^29}║')
    linhas('╚','╝', '═', 60)
    padrao = leiaInt('Escolha: ')
    if padrao == 1:
        nome = 'placar.txt'
        break
    elif padrao == 2:
        print('Não se esqueça do .txt no final')
        nome = str(input('Nome do arquivo: '))
        break
    else:
        print('Opção Inválida, Tente Novamente!')
        sleep(3)
        clear()
        continue
abrir(nome)
while True:
    clear()
#   */ Menu Principal /*
    opc = menu(['Ler Placar', 'Adicionar Pontuação', 'Adicionar Pessoa' ,
     'Remover Pessoa', 'Deletar Arquivo', 'Sair'], 'Ver. 1.1.3')
#   */ Mostra os items já salvos na Tabela /*
    if opc == 1:
        try:
            clear()
            mostrar(organizar(ler(nome)))
            input('Enter pra Continuar')
        except:
            print('Não foi possivel Ler o Placar!')
#   */ Adiciona ou remove pontuação de um participante da tabela /*
    elif opc == 2:
        try:    
            clear()
            mostrar(organizar(ler(nome)))
            modificar(nome, ler(nome))
        except:
            print('Não Foi possivel Adicionar Pontuação!')
            sleep(3)
        else:
            input('Enter para continuar')
#   */ Adiciona um participante a tabela /*
    elif opc == 3:
        try:    
            clear()
            mostrar(organizar(ler(nome)))
            adicionar(nome)
            input('Enter para Continuar')
        except:
            print('Não foi possivel Adicionar Pessoa')
#   */ Remove um participante da tabela /*
    elif opc == 4:
        try:
            clear()
            mostrar(organizar(ler(nome)))
            removerpessoa(nome, ler(nome))
        except Exception as erro:
            print(f'Não Foi possivel remover: {erro.__class__} ')
#   */ Deleta o arquivo que foi aberto e está sendo lido pelo programa /*
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
            delarquivo(nome)
            break
        else:
            continue
#   */ Sair do programa /*
    elif opc == 6:
        print('Saindo do Programa')
        sleep(1)
        print('Até Logo...')
        sleep(1)
        break
# */ Caso o Usuário digite um número que não está na lista o menu é recarregado  /*
    else:
        print('Opção Inválida')
        sleep(2)
        continue
