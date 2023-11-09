rodas = int(input("Digite a quantidade de rodas: "))
peso = int(input("Digite o peso bruto do veiculo em kg: "))
pessoas = int(input("Digite a quantidade de pessoas no veiculo: "))

if (rodas == 2 or rodas ==3):
    print("A melhor categoria de habilitação é A.")

elif (rodas == 4 and pessoas <= 8 and peso <= 3500):
    print("A melhor categoria de habilitação é B.")

elif (rodas >= 4 and (peso >= 3500 and peso <= 6000)):
    print("A melhor categoria de habilitação é C.")

elif (rodas >= 4 and pessoas > 8):
    print("A melhor categoria de habilitação é D.")

elif (rodas >= 4 and peso > 6000):
    print("A melhor categoria de habilitação é E.")