import datetime
class Registro:
    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

nome_informado = input(str("Informe seu nome completo: "))
email_informado = input(str("Informe seu e-mail: "))
nascimento_informado = input(str("Informe sua data de nascimento: "))

registro = Registro(nome=nome_informado, email=email_informado, nascimento=nascimento_informado)


print(f"\nNome: {registro.nome}\nEmail: {registro.email}\nNascimento: {registro.nascimento}")
