# ==========================================
# EXERCÍCIO 10: Função do Dobro
#
# O QUE FAZER:
# Crie uma função chamada 'dobro(numero)' usando 'def'.
# Ela deve receber um número como parâmetro e RETORNAR (return) o dobro dele.
# Depois, peça um número ao usuário, chame a função e mostre o resultado.
# ==========================================

# Escreva seu código aqui:
def dobro(num):
    return num * 2

num = int(input(f"Informe um numero: "))
print(f"O dobro dele é: {dobro(num)}")