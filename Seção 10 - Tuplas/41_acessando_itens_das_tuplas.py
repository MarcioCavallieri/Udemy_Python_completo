tupla = ('Gabriel', 'Márcio', 'André', 34, 'Lucas', "João")

print(tupla)

print(tupla[0])
print(tupla[1])
print(tupla[2])

print(tupla[-1])
print(tupla[-2])
print(tupla[-3])


print(tupla[2:5])
print(tupla[2:])
print(tupla[:5])

print('Márcio' in tupla)
print(34 in tupla)
print('gabriel' in tupla)
print(34.1 in tupla)

if ("sss" in tupla):
    print('sim')
else:
    print('não')