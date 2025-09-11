from time import sleep

def contador(inicio, final, passo):
    passo = abs(passo)
        
    if passo == 0: 
        passo = 1   
    
    print(f'Contagem de {inicio} até {final} de {passo} em {passo}:')
    
     
    
    if inicio < final:
        cont = inicio
        
        while cont <= final:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont += passo
        print('\nFim!\n')
        
    else:
        cont = inicio
        
        while cont >= final:
            print(f'{cont} ', end='')
            sleep(0.25)
            cont -= passo
            
        print('\nFim!\n')
        
contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Inicio:'))
final = int(input('Final:'))
passo = int(input('Passo:'))

contador(inicio, final, passo)