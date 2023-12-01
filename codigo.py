def par_e_impar(lista):
    pares = 0
    impares = 0; par = 'eu'; impar = 'eu'

    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    if pares <= 1:
        par = "par"
    else:
        par = "pares"

    if impares <= 1:
       impar = "ímpar"
    else:
       par = "ímpares"

    return str(pares) + par + ", " + str(impares) + impar
