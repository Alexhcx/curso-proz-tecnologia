def calculadora (num_1, num_2, escolha):
    if escolha == 1:
       return num_1 + num_2
    if escolha == 2:
        return num_1 - num_2 
    if escolha == 3:
        return num_1 * num_2
    if escolha == 4:
        return num_1 / num_2
    else:
        return 0

print("o resultado da operação é",calculadora(10, 2, 1))  # soma = 12
print("o resultado da operação é",calculadora(14, 93, 2)) # subtração = -79
print("o resultado da operação é",calculadora(31, 12, 3)) # multiplicação = 372
print("o resultado da operação é",calculadora(90, 30, 4)) # divisão = 3.0
print("o resultado da operação é",calculadora(10, 2, 5))  # 0  
