tupla = ('Gabriel', 'Márcio', 'André', 34, 'Lucas', "João")

print(tupla)

lista = list(tupla)

print(lista)

lista[3] = 'Daniele'

tupla = tuple(lista)

print(tupla)

lista.append('Thaina')

tupla = tuple(lista)

print(tupla)

tupla2 = ('Beto', 'Dudu')

tupla = tupla + tupla2

print(tupla)