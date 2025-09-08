dados_temp = dict()
dados = list()
gols = list()
partidas = 0

while True:
    total = 0
    dados_temp['nome'] = str(input('Nome jogador: '))
    partidas = int(input('Quantas partidas jogou?'))

    for indice in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {indice + 1} partida?')))
        total += gols[indice]
        
        
    dados_temp['gols'] = gols[:]
    dados_temp['total'] = total
    dados.append(dados_temp.copy())
    gols.clear()
    dados_temp.clear()
        
    resp = str(input('Deseja continuar? [S/N]').upper()[0])
    if resp not in 'SN':
        while True:
            print('Responda com [S/N]')
            resp = str(input('Deseja continuar? [S/N]').upper()[0])
            if resp in 'SN':
                break
            
    if resp in 'N':
        break


print(f'Cód. Nome          Gols         Total')
print('-'*40)
for indice, jogador in enumerate(dados):
    print(f'{indice:<5} {jogador["nome"]:<12} {" | ".join(map(str, jogador["gols"])):<15} {jogador["total"]:<5}')
    
print('-'*40)

while True:
    
    resp = int(input('Deseja ver o desempenho de qual jogador? [digite o cód]'))
    
    if resp == 999:
        break
    
    if resp >= len(dados):
        print('Não existe jogador com esse Cód. tente novamente')
        
    else:    
        print(f'Levantamento de jogador: {dados[resp]['nome'].upper()}')
        print('-'*40)
        for indice in range(0, len(dados[resp]['gols'])):
            print(f'No jogo {indice + 1} fez {dados[resp]['gols'][indice]} gols')
            
        print('-'*40)
        
print('Obrigado por utilizar nosso sistema')