tupla = ('Gabriel', 'Márcio', 'André', 'Lucas', "João")

print(tupla)

for I in tupla:
    print(I)

for I in range(len(tupla)):
    print(tupla[I])

I = 0
while I < len(tupla) - 1:
    print(tupla[I])
    I+=1

[print(x) for x in tupla]