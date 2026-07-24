# ==========================================
# EXERCÍCIO 1: Introdução à POO (Classe e Objeto)
#
# O QUE FAZER:
# 1. Crie uma classe chamada 'Cachorro'.
# 2. Crie um método chamado 'latir()' que exibe: "[Nome] está latindo: Au Au!"
# ==========================================

# Escreva seu código aqui:
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        return f"{self.nome} esta latindo: Au Au!"

c1 = Cachorro("Rex", "Doberman")
print(c1.latir())
