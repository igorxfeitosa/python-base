números = list()

for num in range(0, 5):
    num_user = int(input(f'Digite o {num + 1}° valor'))
    números.append(num_user)

print(f'os valores inseridos foram {números}')
print(f'o maior valor inserido foi: {max(números)} na posição {(números.index(max(números))) + 1}')
print(f'o menor valor inserido foi: {min(números)} na posição {(números.index(min(números))) + 1}')
