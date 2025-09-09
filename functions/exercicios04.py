from random import randint

lista = list()

def sorteando(num):
    num_sorteado = 0
    while True:
        
        num_sorteado = randint(0,   10)
        if num_sorteado not in num:
            num.append(num_sorteado)
        
        if len(num) == 5:
            break
        
    print(f'Valores sorteados: {", ".join(map(str, num))}.')
    
    
def somando_pares(num):
    soma = 0
    lista_soma = list()
    for i in num:
        if i % 2 == 0:
            lista_soma.append(i)
            soma += i
    
    print(f'Somando os valores pares da lista{sorted(lista_soma)}, temos: {soma}.')
    

sorteando(lista)
somando_pares(lista)
