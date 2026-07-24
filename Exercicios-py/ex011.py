# ==========================================
# EXERCÍCIO BÔNUS (11): Maior e Menor sem usar max/min
#
# O QUE FAZER:
# Crie uma lista com 5 números inteiros.
# Descubra qual é o MAIOR e qual é o MENOR número dessa lista
# usando apenas um laço 'for' (sem usar as funções max() e min()).
# ==========================================

# Escreva seu código aqui:
num = [10, 5, 8, 3, 12]
for i in range(len(num)):
    if i == 0:
        maior = num[i]
        menor = num[i]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]

print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")