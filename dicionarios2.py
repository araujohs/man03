#3.a
pessoas = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

#3.b
pessoas[2] = {'nome': 'José', 'idade': 32, 'nacionalidade': 'brasileiro'}
pessoas[3] = {'nome': 'Isabel', 'idade': 22, 'nacionalidade': 'chilena'}
print(pessoas)
print()

#3.d
pessoas_copy = pessoas.copy()

#3.e
pessoas.pop(2)
print(pessoas)
print()

#3.f
pessoas.popitem()
print(pessoas)
print()

#3.g
pessoas.clear()
pessoas_copy.clear()

#3.h
chaves = ('autor','titulo','genero')
valores = ('Machado De Assis','Memórias Póstumas de Brás Cubas','romance')
novo_dicionario = dict.fromkeys(chaves,valores)

#3.i.i
print(novo_dicionario.items())
print()

#3.i.ii
print(novo_dicionario.keys())
print()

#3.i.ii
print(novo_dicionario.values())
print()
