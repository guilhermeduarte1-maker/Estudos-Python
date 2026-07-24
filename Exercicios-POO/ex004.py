# ==========================================
# EXERCÍCIO 4 (POO): Herança Simples (Pessoa e Aluno)
#
# O QUE FAZER:
# 1. Crie uma classe 'Pessoa' com atributos 'nome' e 'idade' no __init__.
# 2. Crie um método 'apresentar()' que exibe: "Olá, meu nome é [nome]."
# 3. Crie uma classe 'Aluno' que HERDA de 'Pessoa'.
# 4. Na classe 'Aluno', adicione o atributo 'matrícula' e um método
#    'estudar()' que exibe: "[nome] está estudando."
# 5. Instancie um Aluno, chame o método 'apresentar()' e o 'estudar()'.
# ==========================================

# Escreva seu código aqui:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, eu sou {self.nome}, e tenho {self.idade} anos."

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def estudar(self):
        return f"{self.nome} esta estudando."

a1 = Aluno("Vitor", 16, 202601)
print(a1.estudar())