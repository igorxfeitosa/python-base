alunos = dict()

alunos['nome'] = str(input('Informe o nome do aluno:'))
alunos['media'] = float(input('Informe a média do aluno:'))

if alunos['media'] >=7:
    alunos['situacao'] = 'Aprovado'
    
elif 4 <= alunos['media'] < 7:
    alunos['situacao'] = 'Recuperação'
    
else: alunos['situacao'] = 'Reprovado'
    
print('=-'*20)
for keys, values in alunos.items():
    print(f'{keys}: {values}')
    
print('=-'*20)