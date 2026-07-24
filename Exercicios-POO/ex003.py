# ==========================================
# EXERCÍCIO 3 (POO): Sistema de Saque com Validação
#
# O QUE FAZER:
# 1. Crie uma classe chamada 'ContaComSaque'.
# 2. No __init__, receba o 'titular' e o 'saldo_inicial'.
# 3. Crie um método 'sacar(valor)':
#    - Se o valor for MENOR ou IGUAL ao saldo, subtraia o valor
#      e exiba: "Saque de R$ [valor] realizado!".
#    - Se o valor for MAIOR que o saldo, NÃO altere o saldo
#      e exiba: "Saldo insuficiente!".
# ==========================================

# Escreva seu código aqui:
class ContaComSaque:
    def __init__(self, titular, saldo_inicial=100):
        self.titular = titular
        self.saldo_inicial = saldo_inicial

    def __str__(self):
        return f"{self.titular} tem R${self.saldo_inicial}"

    def sacar(self, valor):
        if valor <= self.saldo_inicial:
            self.saldo_inicial -= valor
            return f"Saque de R${valor} realizado."
        else:
            return "Saldo insuficiente."

c1 = ContaComSaque("Bruno")
print(c1)
c2 = ContaComSaque("Caio", 200)
print(c2)
print(c2.sacar(240))
print(c2.sacar(130))
print(c2)
