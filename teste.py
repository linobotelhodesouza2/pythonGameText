# Exemplo de como remover dados de uma lista
lista = ['Yoda', 'Luke', 'Darth Vader'] # criando uma lista
print(lista)
lista.pop(1)    # removendo o dado da lista utilizando o .pop() e colocando o valor correspondente a 1 que será o valor de 'Luke' na lista
print(lista)

#exemplo de chave : valor
personagens = {
    'Yoda':'Mestre Jedi',
    'Mace Windu':'Mestre Jedi',
    'Anakin Skywalker':'Cavaleiro Jedi',
    'R2-D2':'Dróide',
    'Dex':'Balconista'
}

for chave in personagens.keys():
    print(chave)

for chave in personagens.items():
    print(chave)

for valores in personagens.values():
    print(valores)

for chave, valor in personagens.items():
    print('O personagem {} pertence a classe {}'.format(chave, valor))

# REMOVENDO UM ITEM DA LISTA
'''personagens.popitem()''' # removendo um valor qualquer da lista
personagens.pop('Anakin Skywalker') #removendo um valor especifico na lista

for chave, valor in personagens.items():
    print('O personagem {} pertence a classe {}'.format(chave, valor))
