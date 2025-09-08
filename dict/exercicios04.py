est_jogador = dict()
gols = list()
total = 0
est_jogador['nome'] = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas {est_jogador['nome']} jogou?'))

for indice in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {indice + 1}? ')))
    total += gols[indice]
    est_jogador['gols'] = gols[:]
    
    
est_jogador['total'] = total
print('=*' * 30)
print(est_jogador)
print('=*' * 30)

for keys, values in est_jogador.items():
    print(f'{keys}: {values}')
    
print('=*' * 30)
    
print(f'O jogador {est_jogador['nome']} jogou {len(est_jogador['gols'])} partidas')
for chave in range(len(est_jogador['gols'])):
    print(f'Na partida {chave + 1}, fez {est_jogador["gols"][chave]}')
    
print(f'Foi um total de {est_jogador['total']}')