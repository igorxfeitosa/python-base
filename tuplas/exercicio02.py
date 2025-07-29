times_camp_br = ('Corinthians', 'Palmeiras', 'Flamengo', 'Cruzeiro', 'Fluminese', 'São Paulo', 'Vasco da Gama', 'Botafogo',
                 'Santos', 'Chapecoense', 'Atlético MG', 'Mirassol', 'Bahia', 'Fortaleza', 'Ceará', 'Internacional', 'Grêmio', 
                 'Bragantino', 'Vitória', 'Sport Recife')

print('Tabela Campeonato Brasileiro')
for pos, time in enumerate(times_camp_br):
    print(f'{pos + 1}. {time}')
    
print('Os primeiros 5 colocados do Brasileirão')
for colocacao in range(0, 5):
    print(f'{colocacao + 1}.{times_camp_br[colocacao]}')
    
print('Os 4 últimos colocados do Brasileirão:')
for colocacao in range(16, 20):
    print(f'{colocacao + 1}. {times_camp_br[colocacao]}')  
   
print('Times em ordem alfabética') 
times = []    
for pos in range (0, len(times_camp_br)):
    times.append(times_camp_br[pos])    

else: print(sorted(times))


print(f'A Chapecoense está na {times_camp_br.index('Chapecoense') + 1}° posição')