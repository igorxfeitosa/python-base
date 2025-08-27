matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma_ter_col = 0
maior_seg_col = 0

for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas][colunas] = int(input(f'Digite um valor para {linhas}, {colunas}: '))
        
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}]', end='')
        if matriz[linhas][colunas] % 2 == 0:
            pares += matriz[linhas][colunas]
    print()          
            

for colunas in range(0, 3):
    if matriz[1][colunas] > maior_seg_col:
        maior_seg_col = matriz[1][colunas]
            
for linhas in range (0, 3):
    soma_ter_col += matriz[linhas][2]
    
    
print(f'A soma dos números pares é de: {pares}')
print(f'A soma dos valores da terceira coluna é de: {soma_ter_col}')
print(f'O maior número da segunda linha é: {maior_seg_col}')

