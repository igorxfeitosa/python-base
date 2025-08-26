valores = list()
pares = list()
impares = list()

while True:
    num = int(input('Digite um número:'))
    valores.append(num)
    
    resp = str(input('Deseja continuar?[S/N]').upper())
    
    if resp in 'Nn':
        break

for val in valores:
    if val % 2 == 0:
        pares.append(val)
        
    else:
        impares.append(val)
        
print(f'Lista completa {valores}')
print(f'Lista de números pares {pares}')
print(f'Lista de números impares {impares}')
