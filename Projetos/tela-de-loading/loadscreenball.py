from os import system
from time import sleep
c = 0
p = 0
while p < 10:
    for c in range(0, 18):
        print()
        print()
        print()
        if c == 0:
            print("""
           ● ● ● ◌
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 1:
            print("""
           ◌ ● ● ● 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 2:
            print("""
           ◌ ◌ ● ● 
         ◌         ●
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 3:
            print("""
           ◌ ◌ ◌ ● 
         ◌         ●
        ◌           ●
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 4:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ●
        ◌           ●
       ◌             ●
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 5:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ●
       ◌             ● 
        ◌           ●
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 6:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ●
        ◌           ●
         ◌         ●
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 7:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ●
         ◌         ●
           ◌ ◌ ◌ ●
            """
            )
        elif c == 8:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ●
           ◌ ◌ ● ●
            """
            )
        elif c == 9:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ● ● ●
            """
            )
        elif c == 10:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ● ● ● ◌
            """
            )
        elif c == 11:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ●         ◌
           ● ● ◌ ◌
            """
            )
        elif c == 12:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ◌             ◌ 
        ●           ◌
         ●         ◌
           ● ◌ ◌ ◌
            """
            )
        elif c == 13:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ◌           ◌
       ●             ◌ 
        ●           ◌
         ●         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 14:
            print("""
           ◌ ◌ ◌ ◌ 
         ◌         ◌
        ●           ◌
       ●             ◌ 
        ●           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 15:
            print("""
           ◌ ◌ ◌ ◌ 
         ●         ◌
        ●           ◌
       ●             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 16:
            print("""
           ● ◌ ◌ ◌ 
         ●         ◌
        ●           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        elif c == 17:
            print("""
           ● ● ◌ ◌ 
         ●         ◌
        ◌           ◌
       ◌             ◌ 
        ◌           ◌
         ◌         ◌
           ◌ ◌ ◌ ◌
            """
            )
        c += 1
        sleep(0.1)
        system('cls')
    p += 1




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