lista = ["maçã", "banana", "cereja", "melão", "melancia", "cogumelo"]

print(lista)
print(lista[0])
print(lista[1])
print(lista[2])

print(lista[-1]) # le de tras pra frente as posições
print(lista[2:5]) # do inicial até o final - 1
print(lista[:4])
print(lista[2:])
print(lista[-4:-1])

if ('melão' in lista):
    print("sim")
else:
    print('não')