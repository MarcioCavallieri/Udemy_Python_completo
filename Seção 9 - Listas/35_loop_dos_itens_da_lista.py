lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

for I in lista:
    print(I)

for I in range(len(lista)):
    print(lista[I])

I = 0
while I < len(lista) - 1:
    print(lista[I])
    I+=1

[print(x) for x in lista]