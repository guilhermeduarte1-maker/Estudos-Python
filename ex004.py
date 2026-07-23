# ==========================================
# EXERCÍCIO 4: Calculadora de Média
#
# O QUE FAZER:
# Peça para o usuário digitar 3 notas (use float).
# Calcule a média simples das 3 notas.
# ==========================================

# Escreva seu código aqui:
n1 = float(input(f"Digite a nota 1(0 a 10): "))
n2 = float(input(f"Digite a nota 2(0 a 10): "))
n3 = float(input(f"Digite a nota 3(0 a 10): "))

media = (n1+n2+n3) / 3

print(f"A media dessas 3 notas é: {media:.2f}")

if media >= 6:
    print(f"Parabens, {media:.2f} voce passou!")
else:
    print(f"Qu pena, {media:.2f} voce reprovou!")
