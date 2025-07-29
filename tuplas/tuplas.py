lanches = ('hamburguer', 'suco', 'pizza', 'pudim')

print(sorted(lanches))

for comida in lanches:
    print(f'eu vou comer {comida}')
    
for cont in range(0, len(lanches)):
    print(f'eu comi {lanches[cont]}')
    
for pos, comida in enumerate(lanches):
    print(f'vou comer {comida}, na posição {pos}')
    
    
a = (2, 4, 6, 8, 10)
b = (1, 3, 5, 7, 9)
c = a + b 

print(c)
print(sorted(c))
print(len(c)) 
print(c.count(2))
print(c.index(4)) 

pessoa = ('igor', 29, 'M', 71.50)

print(pessoa)  
del(pessoa)
   

    