trabalhador = dict()

trabalhador['nome'] = str(input('Nome:'))
trabalhador['idade'] = 2025 - int(input('Ano de Nascimento:'))
trabalhador['CTPS'] = int(input('N° Carteira de Trabalho:'))

if trabalhador['CTPS'] == 0:
    for keys, values in trabalhador.items():
        print(f'{keys}: {values}')

else:
    trabalhador['ano da contratação'] = int(input('Ano da contratação:'))
    trabalhador['salario'] = float(input('Salario:'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + 35
    
    for keys, values in trabalhador.items():
        print(f'{keys}: {values}')