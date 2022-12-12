#Tupla é imutável

tupla = ('Gabriel', 'Márcio', 'André', "André")

print(tupla)
print(len(tupla))

tupla2 = ('carro')

print(type(tupla2))

tupla2 = ('carro', ) #ridiculo, tem q por essa virgula ai pra ele entender que é uma tupla de um item somente

print(type(tupla2))

tupla3 = (1, 5, 4, 25)

print(tupla3)

tupla4 = (1, 'Márcio', False, True, 45.67)

print(tupla4)

tupla5 = tuple((True, 'Márcio', 4))

print(tupla5)