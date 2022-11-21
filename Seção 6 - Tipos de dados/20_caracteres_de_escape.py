txt = "Somos os chamados 'vikings' do norte"
print(txt)

txt = "Somos os chamados \"vikings\" do norte"
print(txt)

txt = "olá \nmundo" # quegra de linha
print(txt)

txt = "olá \rmundo"
print(txt) # ignora o que está antes do \\r

txt = "olá \tmundo"
print(txt) # tab

txt = "It\'s alright"
print(txt)

txt = "Vai inserir um \\ (barra invertida)"
print(txt)

txt = "olá\bmundo" # come um caractere antes, tipo backspace
print(txt)

txt = "\x48\x65\x6c\x6c\x6f" #\x representa hexadecimal
print(txt)

txt = "\110\145\154\154\157" # \ com 3 numeros inteiros representa octal
print(txt)