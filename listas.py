lista_mesclada = [1,2,3,"Olá, Python",True,12.6]
print(lista_mesclada)

lista_mesclada.append(["Lista aninhada"])
print(lista_mesclada)

lista_mesclada.insert(3,5)
print(lista_mesclada)

print(len(lista_mesclada))

lista_mesclada.pop(0)
print(lista_mesclada)

nova_lista_mesclada =[]

for i in range(4):
    nova_lista_mesclada.append(lista_mesclada[i])
print(nova_lista_mesclada)