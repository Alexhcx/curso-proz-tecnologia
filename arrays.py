# Declare dois arrays, cada um com um mínimo de cinco elementos, e imprima eles no terminal usando o comando print(). 
# O primeiro array deve conter os produtos de uma loja da sua escolha (loja de comida, materiais de construção, música, etc). 
# O segundo array deve conter os anos de nascimento de familiares e amigos seus. 
# Lembre-se de usar nomes descritivos para nomear cada variável, e de usar o tipo de dado apropriado para cada lista 
# (strings, booleanos, números inteiros, floats).

Loja_intrumentos_musicais = ["Guitarra Gibson Les Paul Standard", 
                             "Pedaleira Zoom G5n", "Microfone Shure 55SH", 
                             "Kit de palhetas Dunlop 1.0mm", "Contra Baixo Tagima XB21"]

Data_nascimento_amigos = [1989, 1967, 1982, 1992, 1999]

print("PRODUTO DA LOJA DE INSTRUMENTOS MUSICAIS: ")
for i in Loja_intrumentos_musicais:
    print("Produto:", i)

print("\nDATA DE NASCIMENTO DE AMIGOS: ")
for i in Data_nascimento_amigos:
    print("Data de Nascimento:", i)