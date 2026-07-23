# ==========================================
# EXERCÍCIO 7: Validador de Senha Secreta
## ==========================================

# Escreva seu código aqui:

senha = "py123"
while True:
    tent = input("Digite a senha: ")
    if tent == senha:
        print(f"Senha correta!")
        break
    else:
        print("Senha incoreta! tente novamente")
