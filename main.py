from operacoes import calcula_media, aluno_aprovado, lista_reprovados

alunos = {
     26: "Maria",
    101: "Ana",
     13: "João",
     37: "Ágatha",
     72: "Joaquim",
      5: "Félix"
    }

notas = { 
     26: [ 8.0, 7.0, 5.0, 9.0],
    101: [ 9.0, 9.0, 8.0, 9.0],
     13: [ 6.0, 5.0, 5.0, 5.0],
     37: [ 8.0, 6.0, 7.5, 9.0],
     72: [ 6.0, 5.5, 5.0, 7.0],
      5: [10.0, 8.0, 8.0, 8.0]
    }

reprovados = dict()

for aluno in alunos:
    media = calcula_media(notas[aluno])
    aprovado = aluno_aprovado(media)
    if(not aprovado):
       reprovados[aluno] = media #{'media': media}

lista_reprovados(alunos,reprovados)