True
False

x = 10
y = 11

print(y > x)
print(x > y)
print(x == y)

if (x > y):
    print('verdade')
else:
    print('mentira')

print(bool("oi"))
print(bool(""))
print(bool(14))
print(bool(0))

print(bool(()))
print(bool([]))
print(bool({}))

x = 900

print(isinstance(x, int))
print(isinstance(x, bool))
print(isinstance(x, float))