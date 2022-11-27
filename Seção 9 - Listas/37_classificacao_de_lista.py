lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

lista_2 = [40, 23, 1, 56, 70, 9, 100]

lista.sort() # mexe na lista original
lista_2.sort()

print(lista)
print(lista_2)

lista.sort(reverse=True) # mexe na lista original.
lista_2.sort(reverse=True)

print(lista)
print(lista_2)

def funcao(x):
    return abs(x - 20)

lista_2.sort(key=funcao)

print(lista_2)

lista.reverse() # de tras pra frente
lista_2.reverse()

print(lista)
print(lista_2)