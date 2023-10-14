import bcrypt
import random
import string


comprimento = int(input("Digite o comprimento da senha: "))

def gerar_senha(comprimento):
    if comprimento > 4:
        senha = [
            random.choice(string.punctuation),
            random.choice(string.digits) ,
            random.choice(string.ascii_letters),
        ]
        possibilidades = "".join([string.punctuation,string.digits,string.ascii_letters])
        senha.extend(random.choices(possibilidades, k=comprimento-3))

        random.shuffle(senha)
        return "".join(senha)

    else:
        return None 

senha = gerar_senha(comprimento)
hash = bcrypt.hashpw(senha.encode('utf8'),bcrypt.gensalt())


print(hash)
print(senha)