import os, time
c = 0
while c < 57:
    os.system('color 0a')
    os.system('cls')
    cheio = "■" * c
    vazio = "□"* (56 - c)
    print('╔', end='', flush=True)
    print('═' * 58, end='', flush=True)
    print('╗', flush=True)

    print(f'║ {cheio}{vazio} ║', flush=True)

    print('╚', end='', flush=True)
    print('═' * 58, end='', flush=True)
    print('╝', flush=True)
    c += 1
    time.sleep(0)
input('Enter pra continuar')
