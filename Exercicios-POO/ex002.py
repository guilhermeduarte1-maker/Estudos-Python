# ==========================================
# EXERCÍCIO 2 (POO): Conta Bancária Simples
#
# O QUE FAZER:
# 1. Crie uma classe chamada 'ContaBancaria'.
# 2. No __init__, receba o 'titular' e inicie o 'saldo' valendo 0.
# 3. Crie um método 'depositar(valor)' que soma o valor ao saldo.
# 4. Crie um método 'exibir_saldo()' que mostra a mensagem:
#    "Conta de [Titular] possui R$ [Saldo]".
# 5. Instancie uma conta, faça um depósito de qualquer valor
#    e chame o método para exibir o saldo.
# ==========================================

# Escreva seu código aqui:
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def __str__(self):
        return f"{self.titular} possui R${self.saldo}"

    def depositar(self, valor):
        self.saldo += valor
        return f"Agora seu saldo é R${self.saldo}"

    def exibir_saldo(self):
        return f"Conta de {self.titular} possui R${self.saldo}"

c1 = ContaBancaria("Flavio", 70)
print(c1.titular)
print(c1.saldo)

print(c1.exibir_saldo())
print(c1.depositar(30))
print(c1.exibir_saldo())
print(c1)
