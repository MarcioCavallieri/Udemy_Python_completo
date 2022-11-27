lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

lista_2 = []

for x in lista:
    if ("o" in x):
        lista_2.append(x)

print(lista_2)

lista_3 = [x for x in lista if "o" in x]

print(lista_3)

lista_4 = [x for x in range(10) if x % 2 == 0]

print(lista_4)