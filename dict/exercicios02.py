from random import randint
from operator import itemgetter
from time import sleep
sorte = {'Igor': randint(1, 6),
         'Cleyde': randint(1, 6),
         'Sônia': randint(1, 6),
         'Pedro': randint(1, 6)}
         
sorte_organizada = list()
sorte_organizada = sorted(sorte.items(), key=itemgetter(1), reverse=True)

for keys, values in sorte.items():
        print(f'{keys} tirou {values} no dado')
        sleep(1)
        
print()

for indice, values in enumerate(sorte_organizada):
    print(f'O {indice + 1}° Lugar foi {values[0]} que tirou {values[1]}')
    sleep(1)



    
