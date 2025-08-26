valores = [[], []]

for cont in range(0, 7):
    num = int(input(f'Digite {cont + 1}° número:'))
    if num % 2 == 0:
        valores[0].append(num) 
        
    else: 
        valores[1].append(num)
                

print(f'os valores pares digitados foram: {sorted(valores[0])}')
print(f'os valores impares digitados foram: {sorted(valores[1])}')
    
    