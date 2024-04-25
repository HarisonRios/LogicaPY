import random


numero_computador = random.randint(0, 5)


numero_usuario = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))


if numero_usuario == numero_computador:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Que pena! O número escolhido pelo computador era {numero_computador}. Tente novamente!")

