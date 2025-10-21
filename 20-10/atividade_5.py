qtd_notas = int(input("Digite a quantidade de notas fiscais que serão inseridas: "))
soma_das_notas = 0.0

for i in range(1, qtd_notas + 1):
        valor_nota = float(input(f"Digite o valor da nota fiscal nº {i}: R$ "))
        if valor_nota < 0:
            print("O valor da nota não pode ser negativo. Tente novamente.")
            valor_nota = float(input(f"Digite o valor da nota fiscal nº {i}: R$ "))
        soma_das_notas += valor_nota
        i -= 1 

aliquota = 0.0
if soma_das_notas <= 1000.00:
    aliquota = 0.05
elif soma_das_notas < 5000.00:
    aliquota = 0.09
elif soma_das_notas < 15000.00:
    aliquota = 0.12
else:
    aliquota = 0.16

valor_imposto = soma_das_notas * aliquota

print(f"Valor Total das Notas: R$ {soma_das_notas:.2f}")
print(f"Alíquota Aplicada: {aliquota * 100:.0f}%")
print(f"Valor Total do Imposto: R$ {valor_imposto:.2f}")