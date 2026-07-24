# ==========================================
# EXERCÍCIO 5 (POO): Polimorfismo (Sons de Animais)
#
# O QUE FAZER:
# 1. Crie uma classe 'Animal' com um método 'fazer_som()'
#    que exibe: "O animal faz um som."
# 2. Crie uma classe 'Gato' que HERDA de 'Animal' e reescreva
#    o método 'fazer_som()' para exibir: "Miau!"
# 3. Crie uma classe 'Cachorro' que HERDA de 'Animal' e reescreva
#    o método 'fazer_som()' para exibir: "Au Au!"
# 4. Instancie um Gato e um Cachorro e chame 'fazer_som()' nos dois.
# ==========================================

# Escreva seu código aqui:
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        return f"O animal {self.nome} faz um som."
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "Miau!"

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "Au Au!"

animais = [Gato("Nina"), Cachorro("Rex")]

for animal in animais:
    print(f"{animal.nome} faz som: {animal.fazer_som()}")



