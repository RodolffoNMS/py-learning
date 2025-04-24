# Operadores Aritméticos

# Adição
soma = 5 + 2  # 7

# Subtração
subtracao = 5 - 2 # 3

# Multiplicação
multiplicacao = 5 * 2 # 10

# Divisão
divisao = 5 / 2 # 2.5

# Divisão inteira
divisao_inteira = 5 // 2 # 2

# Módulo
modulo = 5 % 2 # 1

# Potência
potencia = 5 ** 2 # 25

# Ordem de Precedência
# 1. ( )
# 2. **
# 3. * / // %
# 4. + -

# Exemplos
5 + 3 * 2 # 5 + (3 * 2) = 5 + 6 = 11
3 * 5 + 4 **2 # 3 * 5 + (4**2) = (3 * 5) + 16 = 15 + 16 = 31
3*(5+4)**2 # 3 * (9) ** 2 = 3* 81 = 243

n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
# Convertendo para float
n1 = float(n1)
n2 = float(n2)
# Convertendo para string
n1 = str(n1)
n2 = str(n2)
# Convertendo para inteiro
n1 = int(n1)
n2 = int(n2)
s  = n1 + n2
m  = n1 * n2
d  = n1 / n1
di = n1 //n2
e  = n1 ** n2

print('A soma é: {}, o produto é {} e a divisão é {}' .format(s, m, d), end = ' ') # A função do end é não pular linha
print('A divisão inteira é: {} e a potência é {}' .format(di, e))


nome = input('Qual o seu nome? ')
# Usando format para alinhar o texto 
print('Olá {:20}, seja bem-vindo(a)!' .format(nome))
print('Olá {:>20}, seja bem-vindo(a)!' .format(nome))
print('Olá {:<20}, seja bem-vindo(a)!' .format(nome))
print('Olá {:^20}, seja bem-vindo(a)!' .format(nome))


print('Olá {:=^20}, seja bem-vindo(a)!' .format(nome))


# Exemplo de ordem de precedência
precedencia = 5 + 2 * 3 - 4 / 2 ** 2

"""
# Operadores de Atribuição
a = 5
b = 2

# Atribuição simples
a = b
print(a) # 2
# Atribuição com adição
a += b
print(a) # 4
# Atribuição com subtração
a -= b
print(a) # 2
# Atribuição com multiplicação
a *= b
print(a) # 4
# Atribuição com divisão
a /= b
print(a) # 2.0
# Atribuição com divisão inteira
a //= b
print(a) # 1.0
# Atribuição com módulo
a %= b
print(a) # 1.0
# Atribuição com potência
a **= b
print(a) # 1.0
# Operadores de Comparação
# Igualdade
igual = (5 == 2)
print(igual) # False
# Diferença
diferente = (5 != 2)
print(diferente) # True
# Maior que
maior = (5 > 2)
print(maior) # True
# Menor que
menor = (5 < 2)
print(menor) # False
# Maior ou igual a
maior_igual = (5 >= 2)
print(maior_igual) # True
# Menor ou igual a
menor_igual = (5 <= 2)
print(menor_igual) # False
# Operadores Lógicos
# E lógico
e_logico = (5 > 2) and (2 < 5)
print(e_logico) # True
# Ou lógico
ou_logico = (5 > 2) or (2 > 5)
print(ou_logico) # True
# Não lógico
nao_logico = not (5 > 2)
print(nao_logico) # False
# Operadores de Identidade
# É o mesmo objeto
a = [1, 2, 3]
b = a
print(a is b) # True
# Não é o mesmo objeto
c = [1, 2, 3]
print(a is not c) # True
# Operadores de Associação
# Pertence a
a = [1, 2, 3]
b = 2
print(b in a) # True
# Não pertence a
c = 4
print(c not in a) # True
"""