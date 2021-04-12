def media_aluno():
    nota1 = int(input("Digite a nota 1: "))
    nota2 = int(input("Digite a nota 2: "))
    nota3 = int(input("Digite a nota 3: "))

    a_soma_notas = nota1 + nota2 + nota3
    a_media_notas = a_soma_notas/3

    print(f'Média do aluno é {a_media_notas}')


a_media_aluno()
