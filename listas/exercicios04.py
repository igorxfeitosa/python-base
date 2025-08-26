valores = list()

while True:
    num = int(input('digite um numero:'))
    valores.append(num)
    
    resp = str(input('deseja continuar? ').upper())
    
    if resp in 'Nn':
        break

print('A) Quantos números foram digitados?')
print(f'Foram digitados {len(valores)} valores')
print('B) A lista de valores, ordenada de forma decrescente:')
print(f'{sorted(valores)}')

print('C) O valor 5 foi digitado?')

if 5 in valores:
    print('O número 5 consta na lista')
    
else: print('O número 5 não consta na lista')
