alunos = []

for i in range(4):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    alunos.append(nome)


contador = 0
aluno_escolhido = alunos[contador]

contador = (contador + 1) % len(alunos)
print(f"O aluno escolhido para apagar o quadro é: {aluno_escolhido}")