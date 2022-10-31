num = 0

while num < 50:
    num = int(input('Digite Um Número Maior Que 50:  '))

h = 1
s = 1
p = 2
num_maximo = num
while num > 1:

    if num%2 == 0:
        h += (num*2-1)/num
        s -= num/(num*num)

    if num%2 == 1:
        h -= (num*2-1)/num
        s += num/(num*num)
    
    num -= 1

contador = 0
potencia = 1

while True:
    
    while contador != num_maximo:
        contador +=1
        mult = contador
        total = 0

        while (mult != 1):
            if contador % mult == 0:
                total += 1
            mult -= 1

        if total == 1:
            p += contador/potencia**3
            potencia += 2

    if contador == num_maximo:
        break

print(f'''O cálculo de H = {h}
O cálculo de S = {s}
O cálculo de P = {p}
 ''')