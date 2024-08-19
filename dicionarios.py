meu_dicionario = { "1":"Python","2":"Java","3":"PHP"}

print(meu_dicionario)

print(type(meu_dicionario))

print(meu_dicionario.get("1"))

dicionario_frutas = dict(
    chave1={"nome":"limão" , "tipo":"ácida"},
    chave2={"nome":"laranja" , "tipo":"ácida"},
    chave3={"nome":"manga" , "tipo":"semiácida"},
    chave4={"nome":"maça" , "tipo":"semiácida"},
    chave5={"nome":"banana" , "tipo":"doce"},
    chave6={"nome":"mamão" , "tipo":"doce"}
)

print(dicionario_frutas["chave1"]["nome"])
print(dicionario_frutas["chave1"]["tipo"])
print(dicionario_frutas["chave2"]["nome"])
print(dicionario_frutas["chave2"]["tipo"])


for fruta in dicionario_frutas:
    print(dicionario_frutas[fruta]['nome'])
