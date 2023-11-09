import time

#minha solução
intervalo = 1

while(intervalo < 46):
    print(intervalo, "segundos")
    if(intervalo == 45):
        print("Fim do descanso!")
    intervalo = intervalo + 1

#solução do curso

tempoInicial = 1
tempoFinal = 45

print("Iniciando descanso...")

for i in range(tempoInicial,tempoFinal+1):
    print(i)

time.sleep(1)

print("Fim do descanso!")
