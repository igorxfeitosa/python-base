nomes_notas = list()
temp = list()

while True:
    temp_notas = 0
    temp.append(str(input('Digite o nome do aluno:')))
    temp.append(float(input('Digite a 1° nota:')))
    temp.append(float(input('Digite a 2° nota:')))
    
    for linhas in range(1, 3):
        temp_notas += temp[linhas]
        
    temp_notas = temp_notas / 2
    temp.append(temp_notas)
    
    resp = str(input('Deseja continuar? [S/N]').upper())
    nomes_notas.append(temp[:])
    temp.clear()
    
    if resp in 'Nn':
        break
    
print('-'*20)    
print(f'No.  Nome     Média')
print('-'*20 )

for linhas in range(0, len(nomes_notas)):
        print(f'{linhas})   {nomes_notas[linhas][0]:<6}      {nomes_notas[linhas][3]}')

print('-'*20 )    

while True:

    resp = int(input('Digite o código do aluno para ver suas notas:'))
    print(f'\nAs notas de {nomes_notas[resp][0]} foram: | {nomes_notas[resp][1]} | {nomes_notas[resp][2]} | ')

    resp = str(input('Deseja consultar notas de outro aluno?[S/N]').upper())
    
    if resp in 'Nn':
        break

print('\nObrigado, volte sempre!')