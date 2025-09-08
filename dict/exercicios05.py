dados = list()
dados_temp = dict()
media = 0.0

while True:
    dados_temp['nome'] = str(input('Nome:'))
    dados_temp['sexo'] = str(input('Sexo: [F/M]').upper()[0])
    if dados_temp['sexo'] not in 'FM':
        while True:
            print('Responda com [F/M]')
            dados_temp['sexo'] = str(input('Sexo: [F/M]').upper()[0])
            if dados_temp['sexo'] in 'FM':
                break
    
    dados_temp['idade'] = int(input('Idade:'))
    media += dados_temp['idade']
    
    resp = str(input('Deseja continuar? [S/N]').upper()[0])
    if resp not in 'SN':
        while True:
            print('Responda com [S/N]')
            resp = str(input('Deseja continuar? [S/N]').upper()[0])
            if resp in 'SN':
                break
        
    dados.append(dados_temp.copy())
    dados_temp.clear()
    if resp in 'Nn':
        break
    
media = media/len(dados)
print('=-'*30)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas')
print('=-'*30)
print(f'B) A média de idade é de {media} anos')
print('=-'*30)
print('C) As mulheres cadastradas foram:', end=' ')
for i in range(0, len(dados)):
    if dados[i]['sexo'] in 'Ff':
        print(f'{dados[i]['nome']}', end=' ')
print()
print('=-'*30)
print('D) Lista de pessoas acima da média: ')
for i in range(0, len(dados)):
    if dados[i]['idade'] > media:
        print(f'| Nome:{dados[i]['nome']} | Sexo:{dados[i]['sexo']} | Idade:{dados[i]['idade']} |')
print('=-'*30)
