x = "incrível"

def minhaFuncao():   
    x = "fantástico"
    global s
    s = 'teste'
    print('Python é ' + x)    

minhaFuncao()

print('Python é ' + x)

print(s)