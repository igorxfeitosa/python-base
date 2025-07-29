numeros = list()

while True:
    num = int(input('digite um valor'))
    if not num in numeros:
        numeros.append(num)
        
        resp = str(input('deseja continuar? ').upper())
        if resp in 'Nn':
            break
        
        
    else:
        resp = str(input('deseja continuar? ').upper())
        if resp in 'Nn':
            break
        
       
        
   
print(f'{sorted(numeros)}')
