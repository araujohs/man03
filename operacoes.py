def calcula_media(notas):
    media = sum(notas)/len(notas)
    return media

def aluno_aprovado(media):
    resultado = True
    if(media<6.0):
        resultado = False

    return resultado

def lista_reprovados(alunos,reprovados):
    for a in alunos:
        if(a in reprovados.keys()):
            print('Aluno Reprovado: ',alunos[a],
            ' - Matrícula: ',a,
            ' - Média Final: ',reprovados[a])

