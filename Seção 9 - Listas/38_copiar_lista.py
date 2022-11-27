lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

print(lista)

lista_2 = lista # somente referencia

lista.append('uva')

print(lista)
print(lista_2)

print(lista)

lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

lista_2 = lista.copy() # ou list(nomes)

lista.append('uva')

print(lista)
print(lista_2)