lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]


print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

lista[1] = "jabuticaba"

print(lista)

lista[2:5] = ['laranja', 'limão', 'lima']

print(lista)

lista[1:3] = ['morango', 'carambola', 'abacate', 'jaca']

print(lista)

lista[1:3] = ['uva']

print(lista)

lista.insert(5, "pitaia")

print(lista)