expressao = str(input('Digite a expressão:'))
parenteses_1 = expressao.count('(')
parenteses_2 = expressao.count(')')

if parenteses_1 == parenteses_2:
    print('Sua expressão está correta')
    
else: print('Sua expressão está incorreta')