# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def calculaIdade(nome, anoNascimento):
    return nome + " tem " + str(2023 - anoNascimento) + " anos."

while True:
    try:
        nome = input("Digite seu nome completo: ")
        anoNascimento = int(input("Digite seu ano de nascimento: "))
        if 1922 <= anoNascimento <= 2021:
            print(calculaIdade(nome, anoNascimento))
            break
        else:
            print("Ano de nascimento inválido. Digite um ano entre 1922 e 2023.")
    except ValueError:
        print("Valor inválido. Digite um número inteiro para o ano de nascimento.")

