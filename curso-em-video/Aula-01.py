# Print:

print("Olá Mundo!")

# Somando:
print(7 + 4)

# Concatenando
print("7" + "4")
print(7, 4)

# Em Python, todas as variáveis é um objeto.

nome  = "Rodolffo"
idade = 25
peso  = 108.5
# Nesse caso, a concatenação, deve ser com vírgula.
print(nome, idade, peso)

#Para usar o "+" no print, devemos ter variáveis do mesmo tipo:
nome2 = "Rodolffo"
nome3 = "Sarah"
print(nome2 + nome3)


idade2 = 10
idade3 = 15
print(idade2 + idade3)

###############################################################


nome = input ("Digite seu nome:")
print("Olá ", nome, "Seja bem vind@!")

mes = input ("Seu dia de nascimento: ")
dia = input ("Seu mês de nascimento: ")
ano = input ("Seu ano seu nascimento: ")

print(nome, ",você nasceu no dia ", dia, "de", mes, "de", ano, "correto?")

numero1 = input("Primeiro valor")
numero2 = input("Segundo valor")
soma = numero1 + numero2
print("Soma:", soma)

# Você pode fazer a soma dentro do print(), 
# mas precisa garantir que os valores são convertidos para um tipo numérico antes de somá-los. 

numero1 = int(input("Primeiro valor: "))
numero2 = int(input("Segundo valor: "))
print("Soma:", numero1 + numero2)
