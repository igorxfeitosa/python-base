pessoas_pesos = []
temp = []
maior = menor = 0

while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    
    if len(pessoas_pesos) == 0:
        maior = menor = temp[1]
        
    else:
        if temp [1] > maior:
            maior = temp[1]
            
        if temp [1] < menor:
            menor = temp[1]
    
    
    pessoas_pesos.append(temp[:])
    temp.clear()
    
    
    resp = str(input('Deseja continuar? [S/N]').upper())
    
    if resp in 'Nn':
        break
    
print(f'Ao todo foram cadastrados {len(pessoas_pesos)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for maior_peso in pessoas_pesos:
    if maior_peso[1] == maior:
        print(f' {maior_peso[0]}', end='')

print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for menor_peso in pessoas_pesos:
    if menor_peso[1] == menor:
        print(f' {menor_peso[0]}', end='')
    

