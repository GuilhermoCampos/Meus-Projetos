from os import system
from time import sleep
c = 0
while c < 100:
    for c in range(0, 4):
        print()
        print()
        print()
        if c == 0:
            print(f'{"●":>7}')
        elif c == 1:
            print()
            print(f'{"●":>9}')
        elif c == 3:
            print()
            print(f'{"●":>5}')
        elif c == 2:
            print()
            print()
            print(f'{"●":>7}')

        c += 1
        sleep(0.2)
        system('cls')




# 1 2 4 6 8 16 32 64 128 256 512 1024 2048 4096 8192
# 16 32 64 128 256 512 1024 2048 4096 8192 16384
# 1 2 3 4 5 6 7 8 9 A B C D E F 
# 22 = 16
# 642 = 282

#           ● ● ● ●
#         ●         ●
#        ●           ●
#       ●             ● 
#        ●           ●
#         ●         ●
#           ● ● ● ●