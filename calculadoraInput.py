# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

def realizarOperacao(escolha, num1, num2):
    if escolha == 1:
        return "O resultado da soma é: " +  str(num1 + num2)
    elif escolha == 2:
        return "O resultado da subtração é: " +  str(num1 - num2)
    elif escolha == 3:
        return "O resultado da multiplicação é: " +  str(num1 * num2)
    elif escolha == 4:
        return "O resultado da divisão é: " +  str(num1 / num2)
    else:
        return "Essa opção não existe"

print("Bem vindo a Calculadora, escolha a operação que deseja realizar:")
print("1: Soma", "2: Subtração", "3: Multiplicação", "4: Divisão", "0: Sair", sep="\n")
escolha = int(input("Digite o número: "))

while escolha != 0:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(realizarOperacao(escolha, num1, num2))

    print("1: Soma", "2: Subtração", "3: Multiplicação", "4: Divisão", "0: Sair", sep="\n")
    escolha = int(input("Digite o número: "))

print("Obrigado por usar a calculadora!")