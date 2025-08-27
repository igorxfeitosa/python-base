from random import randint
from time import sleep
mega_sena = list()
temp = list()
qnts_jogos = int(input('Quantos jogos deseja sortear? '))

total = 1

while total <= qnts_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        
        if num not in temp:
            temp.append(num)
            cont += 1
        
        if cont >= 6:
            break
        
    temp.sort()
    mega_sena.append(temp[:])
    temp.clear()
    total += 1
    
print('-=' * 5, f'Sorteando {qnts_jogos} jogos', '-=' * 5)
for indice, linha in enumerate(mega_sena):
    print(f'Jogo {indice + 1}: {linha}')
    sleep(1)
    
print('-=' * 6, f'< Boa Sorte >', '-=' * 6)