num_meses = int(input("Digite o número total de meses a serem analisados: "))

consumo_total_kwh = 0.0
valor_total_pago = 0.0
mes_maior_consumo = 0
maior_consumo_kwh = -1.0 

for i in range(1, num_meses + 1):
    consumo_mes_kwh = float(input(f"Digite o consumo em kWh do mês {i}: "))
    
    tarifa_por_kwh = 0.0
    if consumo_mes_kwh <= 100:
        tarifa_por_kwh = 0.55
    elif consumo_mes_kwh <= 200:
        tarifa_por_kwh = 0.70
    else:
        tarifa_por_kwh = 0.95

    custo_mensal = consumo_mes_kwh * tarifa_por_kwh
    print(f"Tarifa aplicada: R$ {tarifa_por_kwh:.2f}/kWh. Custo do mês: R$ {custo_mensal:.2f}")

    consumo_total_kwh += consumo_mes_kwh
    valor_total_pago += custo_mensal
    if consumo_mes_kwh > maior_consumo_kwh:
        maior_consumo_kwh = consumo_mes_kwh

print("\n--- Relatório Final de Consumo de Energia ---")

if num_meses > 0:
    media_mensal_consumo = consumo_total_kwh / num_meses
    print(f"Média de consumo mensal: {media_mensal_consumo:.2f} kWh")
    if media_mensal_consumo > 180:
        print("Status: Alerta! O consumo médio está elevado. Sugerir medidas de economia.")
    else:
        print("Status: Consumo médio dentro dos limites normais.")
else:
    print("Nenhum mês foi analisado.")
print(f"\nConsumo Total no Período: {consumo_total_kwh:.2f} kWh")
print(f"Valor Total Pago: R$ {valor_total_pago:.2f}")
if mes_maior_consumo > 0:
    print(f"Pico de Consumo: Mês {mes_maior_consumo} com {maior_consumo_kwh:.2f} kWh.")