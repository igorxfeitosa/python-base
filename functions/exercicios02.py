from time import sleep

def contador():
    cont = list()
    print(f'Contagem de 1 até 10 de 1 em 1:')
    for i in range(1, 11):
        print(f'{i}', end=' ')
        sleep(0.3)
    print(f'Fim!')
        
    
    print('\nContagem de 10 até 0 de 2 em 2:')
    for i in range(0, 11, 2):
        cont.append(i)
    
    
    cont.sort(reverse=True)
    for i in cont:
        print(f'{i}', end=' ')
        sleep(0.3)
     
    print(f'Fim!')     
    print() 
    cont.clear()
    inicio = int(input('Inicio:'))
    final = int(input('Final:'))
    passo = int(input('Passo:'))
    
        
    if final > inicio:
        print(f'Contagem de {inicio} até {final} de {passo} em {passo}:')
        for i in range(inicio, final, passo):
            cont.append(i)
        
        for i in cont:
            print(f'{i}', end=' ')
            sleep(0.3)
        print(f'Fim!') 
        
        
    if final < inicio:
        print(f'Contagem regressiva de {final} até {inicio} de {passo} em {passo}:')
        for i in range(final, inicio + passo, passo):
            cont.append(i)
            
        cont.sort(reverse=True) 
            
        for i in cont:
            print(f'{i}', end=' ')
            sleep(0.3)
        print(f'Fim!')     
            
        
contador()