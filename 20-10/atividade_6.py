custo_fixo_lote = 500.00
qtd_itens = 100
taxa_desperdicio = 0.05
custo_materia_prima_item = float(input("Digite o custo da matéria-prima por item: R$ "))

custo_variavel_total = 0.0

for item in range(qtd_itens):
    desperdicio_material = custo_materia_prima_item * taxa_desperdicio
    custo_de_um_item = custo_materia_prima_item + desperdicio_material
    custo_variavel_total += custo_de_um_item
custo_total_producao = custo_fixo_lote + custo_variavel_total
margem_lucro = 0.0
if custo_total_producao < 3000.00:
    margem_lucro = 0.35
elif 3000.00 <= custo_total_producao <= 5000.00:
    margem_lucro = 0.20
else:
    margem_lucro = 0.15

preco_minimo_venda_item = (custo_total_producao / qtd_itens) * (1 + margem_lucro)

print(f"Custo Total de Produção do Lote: R$ {custo_total_producao:.2f}")
print(f"Margem de Lucro Mínima Aplicada")