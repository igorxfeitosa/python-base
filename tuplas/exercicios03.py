from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), 
           randint(1,10), randint(1,10))

print('os numeros sorteados foram:')
for n in numeros:
    print(f'{n} ', end='')
    
print(f'o maior número sorteado foi {max(numeros)}')
print(f'o menor número sorteado foi: {min(numeros)}')
    