# ==========================================
# EXERCÍCIO 6: Maior de Três
#
# O QUE FAZER:
# Peça para o usuário digitar 3 números inteiros.
# O programa deve verificar e exibir qual é o MAIOR número.
# ==========================================

# Escreva seu código aqui:
n1 = int(input(f"Digite um numero: "))
n2 = int(input(f"Digite um numero: "))
n3 = int(input(f"Digite um numero: "))

maior = max(n1,n2,n3)
print(f"O maior numero dentre os 3 é: {maior}")