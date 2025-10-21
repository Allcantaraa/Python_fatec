valor_inicial_investimento = float(input("Digite o valor inicial do Investimento: "))
num_meses = int(input("Número de meses a serem simulados: "))
valor_acumulado = valor_inicial_investimento
juros_totais = 0.0

for i in range(1, num_meses + 1):

    taxa_crescimento_mensal = float(input(f"Digite a taxa de crescimento para o mês {i} (em decimal, ex: 0.02 para 2%): "))
    
    juros_mes = 0.0

    if taxa_crescimento_mensal > 0.015:
        juros_mes = valor_acumulado * taxa_crescimento_mensal
        print(f"Rendimento do mês (taxa normal): R$ {juros_mes:.2f}")
    elif 0.005 <= taxa_crescimento_mensal <= 0.015:
        juros_mes = valor_acumulado * taxa_crescimento_mensal * 0.9
        print(f"Rendimento do mês (com penalidade de 10%): R$ {juros_mes:.2f}")
    else:
        juros_mes = 0.0
        print("Rendimento do mês: R$ 0.00 (taxa muito baixa)")

    valor_acumulado += juros_mes
    juros_totais += juros_mes
    
    print(f"Saldo acumulado ao final do mês {i}: R$ {valor_acumulado:.2f}")

print("\n--- Resultado Final do Investimento ---")

if juros_totais > (valor_inicial_investimento * 0.10):
    print("Classificação: Investimento de Alto Sucesso! (Retorno superior a 10%)")
else:
    print("Classificação: Investimento Moderado. Retorno abaixo do esperado.")

print(f"Valor Acumulado Final: R$ {valor_acumulado:.2f}")
print