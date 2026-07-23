# ==========================================
# EXERCÍCIO 9: Contagem de Vogais
#
# O QUE FAZER:
# Peça ao usuário para digitar uma palavra ou frase.
# O programa deve contar quantas VOGAIS (a, e, i, o, u)
# existem no texto digitado e exibir o resultado.
# ==========================================

# Escreva seu código aqui:
#vogais = [a,e,i,o,u]

text = input("Digite um texto: ")

c_v = 0
for p in text:
    if p.lower() in "aeiou":
        c_v += 1
print(f"Esse texto tem {c_v} vogais.")
