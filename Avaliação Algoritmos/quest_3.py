populacao_a = 15000
taxa_a = 0.1

populacao_b = 45000 
taxa_b = 0.05

populacao_c = 65000
taxa_c = 0.025

anos = 0

while populacao_b > populacao_a:
    anos += 1
    populacao_a += (populacao_a * taxa_a)
    populacao_b += (populacao_b * taxa_b)


print(f'A população A irá se igualar ou ultrapassar a B em {anos} anos')

#######################
populacao_a = 15000
taxa_a = 0.1

populacao_b = 45000 
taxa_b = 0.05

populacao_c = 65000
taxa_c = 0.025

anos = 0

while True:
    populacao_a += populacao_a*taxa_a
    populacao_c += populacao_c*taxa_c
    anos += 1
    diferenca = (populacao_a / populacao_c -1) * 100

    if diferenca > 23:
        break
print(f'Irá demorar {anos} para População A passar em 23% População C')