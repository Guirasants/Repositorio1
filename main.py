import random
caracteres = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamanho_senha = int(input("Digite o tamanho da senha: "))
senha = ""
for i in range(senha):
    senha += random.choice(caracteres)
print(senha)