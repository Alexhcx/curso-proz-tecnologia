print()
print("resolução usando for")
for i in range(20, 0, -1):
    if(i != 13):
        print("Andar", i)

print()
print("resolução usando while")
andar = 20
while(andar > 0):
    if(andar != 13):
        print("Andar", andar)
    andar = andar - 1