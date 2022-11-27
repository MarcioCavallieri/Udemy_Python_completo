lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

lista_2 = ['1', '2', '3']

lista_3 = lista + lista_2

print(lista)
print(lista_2)
print(lista_3)

lista_3 = []
lista_3.extend(lista + lista_2)

print(lista)
print(lista_2)
print(lista_3)