import random

while(True):
    lottoQuantity = int(input("로또를 몇장 살꺼야 경태상?"))
    if lottoQuantity <= 0:
        print("왜 안사시는 거죠?.")
        break
    while lottoQuantity>0:
        print("일등 가즈아!!")
        for i in range(1,lottoQuantity+1):
            print("[%d]: " % i, end=" ")
            for j in range(6):
                print("{0:3d}".format(random.randint(1,45)), end=" ")
            print()
        break