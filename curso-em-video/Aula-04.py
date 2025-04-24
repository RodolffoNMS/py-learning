# import usado para importar bibliotecas e módulos.
# Exemplo: import math (importa a biblioteca math)
'''
A função math possui várias funções matemáticas, como:
ceil
floor
trunc
pow
sqrt
log
factorial
'''
# Em Python, podemos importar somente partes de um módulo ou biblioteca.
# Exemplos: 
# from math import sqrt (importa somente a função sqrt da biblioteca math)
# from math import sqrt, pow (importa as funções sqrt e pow da biblioteca math)
# from math import * (importa todas as funções da biblioteca math)
################################################################################

import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# Printa com uma precisão significativa
print('A raiz de {} é igual a {}' .format(num, raiz))
# Printa com arredondamento 'para cima'
print('Valor arredondado: {}'.format(math.ceil(raiz)))
# Printa com arredondamento 'para baixo'
print('Valor arredondado: {}'.format(math.floor(raiz)))
# Printa com uma precisão de somente 2 dígitos
print('Valor com 2 casas decimais: {:.2f}' .format(raiz))
# Printa somente o valor inteiro
print('Valor inteiro: {}'.format(math.trunc(raiz)))
