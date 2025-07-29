itens = ('lápis', 1.90, 'borracha', 2, 'régua', 3.5,
         'caderno', 15.90, 'estojo', 5.40
         )

print(itens)
print('-' * 39)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 39)

for item in range(0, len(itens)):
    if item % 2 == 0:
        print(f'{itens[item]:<30}', end='')
    else: print(f'R${itens[item]:>7.2f}')
    
print('-' * 39)

for item in range(0, len(itens), 2):
    print(f'{itens[item]:<34}', end='')
    print(f'R$ {itens[item + 1]:>7.2f}')
    
print('-' * 45)