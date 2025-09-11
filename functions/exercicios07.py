def fatorial(num, mostrar=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param mostrar: (opcional) mostrar o calculo completo na chamada
    :return: retorna o valor do Fatorial do número desejado  
    """
    
    fatorial = 1
    
    for i in range(num, 0, -1):
        if mostrar == True:
            print(f'{i}', end='')
            if i > 1:
                print(' x ', end='')
            else: print(' = ', end='')
            
            
        fatorial *= i
        
    return fatorial
    
    
print(fatorial(10, mostrar=True))
help(fatorial)