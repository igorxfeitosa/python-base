def leia_int():
    
    while True:
        num = str(input('Número:'))
        if num.isnumeric():
            num = int(num)
            break
            
        else:
            print('Erro! Digite um número válido.')
            
            
    return num



numero = leia_int()
print(f'Você acabou de digitar o número {numero}.')