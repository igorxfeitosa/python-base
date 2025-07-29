#!/usr/bin/env python

__version__ = '0.0.1'
__author__ = 'Igor Feitosa'
__license__ = 'unlicense'


#dunder = substitui a necessidade de falar double underscore ou underline

print ('hello, world')

#programa para descobrir o antecessor e sucessor de um numero
numero = int(input("digite um numero:"))
antecessor = numero - 1
sucessor = numero + 1

print('Analisando o valor {}, o seu antecessor é {}, e o sucessor é {} ' .format(numero, antecessor, sucessor))

#programa para descobrir o dobro, triplo e raiz quadrada de um numero
numero = int(input('digite um numero:'))
dobro = numero * 2
triplo = numero * 3
rq = numero ** (1/2)

print('analisando o valor {}, o Dobro é {}, o Triplo é {}, e a Raiz Quadrada é {:.2f}' .format(numero, dobro, triplo, rq))


#programa para descobrir a media Aritmetica
num1 = float(input('digite o primeiro valor:'))
num2 = float(input('digite o segundo valor:'))

media = (num1 + num2) / 2

print('a media dos numeros {} e {} é de: {:.1f}'.format(num1, num2, media))




