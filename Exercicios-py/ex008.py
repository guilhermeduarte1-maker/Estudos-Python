# ==========================================
# EXERCÍCIO 8: Somador de Números em Lista
## ==========================================

# Escreva seu código aqui:
num = [2, 7, 16, 47, 69]
soma = sum(num)
print(f"a soma da lista é {soma}")

#ou

soma = 0
for i in range(len(num)):
    soma = soma + num[i] 
print(f"Soma por for: {soma}")
