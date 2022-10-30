salario = float(input('Salário: R$'))
vendas = float(input('Vendas: R$'))
if vendas <= 1500:
    bonus = vendas * 0.05
elif vendas > 1500:
    bonus = (1500 * 0.05) + ((vendas - 1500) * 0.07)
salario_final = salario + bonus

print(f'O salário final será de R${salario_final:.2f}')