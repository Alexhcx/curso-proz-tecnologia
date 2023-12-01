lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 

for i in range(len(lista_produtos)):
    print("Temos {} à venda!".format(lista_produtos[i]))

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"
lista_produtos.pop(7)
lista_produtos.append("kit de maquiagem")
lista_produtos.append("pincéis de maquiagem")
print(lista_produtos) 

