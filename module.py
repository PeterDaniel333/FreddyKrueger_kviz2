import os
import time


print("Az időd mérve van,melyet a végén fogsz látni.")
time.sleep(2)
print('1000 ft-al kezded a quizt. minden helyes válasz +1000FT, minden helytelen -500FT.')
time.sleep(3)

class Tesztkerdes:
    def __init__(self, feladvany:str, a:str, b:str, c:str, megoldas:str):
        self.feladvany = feladvany
        self.a = a
        self.b = b
        self.c = c
        self.megoldas = megoldas


def get_teszt() -> list[Tesztkerdes]:
    tesztsor:list[Tesztkerdes] = []
    kerdesek_file = open('teszt.txt', encoding='utf-8-sig')
    megoldasok_file = open('megoldas.txt', encoding='utf-8-sig')
    for x in range(15):
        k:str = kerdesek_file.readline().strip()
        a:str = kerdesek_file.readline().strip()
        b:str = kerdesek_file.readline().strip()
        c:str = kerdesek_file.readline().strip()
        m:str = megoldasok_file.readline().strip()
        tesztsor.append(Tesztkerdes(k, a, b, c, m))
    return tesztsor


def game_loop(tesztsor:list[Tesztkerdes]) -> int:
    pontszam:int = 0
    penz = 1000
    for f in tesztsor:
        print(f.feladvany)
        print(f'\t{f.a}')
        print(f'\t{f.b}')
        print(f'\t{f.c}')
        valasz:str = input('\nHelyes válasz betűjele: ')
        if valasz.lower() == f.megoldas.lower():
            pontszam += 1
            penz += 1000
        else:
            print(f'ez nem nyert, a helyes válasz: {f.megoldas}')
            penz -= 500
        time.sleep(1)
        os.system('cls')
    time.sleep(3)
    print(f"Ennyi pénzzel végeztél: {penz}FT")
    return pontszam

