def escreva(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(msg.center(tamanho))
    print('-' * tamanho)
    
    
palavra = str(input('Palavra:'))
escreva(palavra)