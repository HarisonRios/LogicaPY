## Essa foi feito com ajuda do stackowerflow e chatgpt, pois não consigo entender quase nada

import random

alunos = []

for i in range(4):
    nome = input(f'Digite o nome do {i+1}º aluno: ')
    alunos.append(nome)


for i in range(len(alunos)):
    indice_aleatorio = random.randint(0, len(alunos) - 1)
    alunos[i], alunos[indice_aleatorio] = alunos[indice_aleatorio], alunos[i]

print('A ordem de apresentação dos trabalhos é:')
for aluno in alunos:
    print(aluno)