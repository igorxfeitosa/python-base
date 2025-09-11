def player_status(nome = '<desconhecido>', gols = 0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome = str(input('Nome:'))
gols = str(input('Gols:'))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
    
if nome.strip() == '':
    print(player_status(gols = gols))
    
else:
    print(player_status(nome, gols))



