valores = list()

for cont in range(0, 5):
    num = int(input('digite um valor:'))
    if cont == 0 or num > valores[-1]:
         valores.append(num)
         
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos += 1
            
print(valores)