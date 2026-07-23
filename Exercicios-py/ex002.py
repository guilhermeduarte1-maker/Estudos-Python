# ==========================================
# EXERCÍCIO 2: Par ou Ímpar?
#
# O QUE FAZER:
# Peça para o usuário digitar um número inteiro.
# Verifique se o número é PAR ou ÍMPAR e mostre o resultado.
# ==========================================

# Escreva seu código aqui:
num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print(f"{num} é par.")
else: 
    print (f"{num} é impar.")