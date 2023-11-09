def calcularImc(peso,altura):
    imc = peso/(altura**2)

    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 35:
        return "Obesidade grau 1"
    elif imc >= 35 and imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"    

print(calcularImc(80,1.80))

def operacao(num_lim, incre):
    contador = 0
    for i in range(0, num_lim, incre):
        contador = contador + 1
    return contador

print(operacao(10, 2))
