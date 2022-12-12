tupla = ('Gabriel', 'Márcio', 'André', 'Lucas', "João")

print(tupla)

(a, b, c, d, e) = tupla

print(a)
print(b)
print(c)
print(d)
print(e)

(a, b, *c) = tupla #Coloca o resto como array na variável com o '*'

print(a)
print(b)
print(c)