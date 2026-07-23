# ==========================================
# EXERCÍCIO 5: Tabuada
#
# O QUE FAZER:
# Peça um número inteiro ao usuário e mostre a
# tabuada dele de 1 a 10.
# ==========================================

# Escreva seu código aqui:
num = int(input(f"Digite um numero inteiro: "))

for i in range(1,11):
    r = num*i
    print(f"{num} x {i}: {r}")