numeros = (int(input('digite o primeiro numero')), 
           int(input('digite o segundo numero')),
           int(input('digite o terceiro numero')),
           int(input('digite o quarto numero'))
           )
print(f'os numeros digitados foram {numeros}')
print(f'o numero 9 apareceu {numeros.count(9)} vezes')
print(f'o numero 3 apareceu na {numeros.index(3) + 1}° posição')

for cont in numeros:
    if cont % 2 == 0:
        print(f'os numeros pares digitados foram: {cont}')