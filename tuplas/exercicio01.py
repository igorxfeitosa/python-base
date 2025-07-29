numero_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
              'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    numero = int(input('digite um numero entre 0 e 20'))

    if numero >=0 and numero <=20:
        print('você digitou o número:', numero_ext[numero])
        continuar = input('Gostaria de continuar?').upper()
        if continuar in 'Nn':
            print('Obrigado por utilizar nosso sistema')
            break
    else:
        print('Digite um número no intervalo de 0 e 20')