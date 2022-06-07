from re import S
from module import game_loop, get_teszt
from timeit import default_timer as timer
from datetime import timedelta
import time
m = input('Add meg a neved: ')
start = timer()
print(f'Sok sikert,{m} ')
time.sleep(3)
teszt = get_teszt()
pontszam:int = game_loop(teszt)
print(f'elért pontszám: {pontszam}/15')
time.sleep(3)
end = timer()
print(f'Ennyi idő alatt sikerült teljesitened a Quizt, {m}: {(timedelta(seconds=end-start))}')