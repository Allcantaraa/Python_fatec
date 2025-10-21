salario_base_sem = float(input("Digite o salario base semanal: "))

folhas_toleradas = 1

for i in range(5) :
    pontuacao_produtividade = float(input("Pontuação de Produtividade Diária: "))

    if pontuacao_produtividade < 60 :
        contagem_falhas = 0

produtividade_media = (folhas_toleradas) / 5

if produtividade_media > 80 and contagem_falhas <= 1 :
    print("Pagamento Máximo: Bônus de 10% aplicado.")
    pagamento_final = salario_base_sem * 1.10
elif produtividade_media >= 60 and produtividade_media <= 80 or contagem_falhas > 1 :
    print("Pagamento Padrão: Penalidade de 5% aplicada (Devido a falhas).")
    pagamento_final = salario_base_sem * 0.95
else :
    print("Senalidade Severa: Pagamento reduzido em 25%.")
    pagamento_final = salario_base_sem * 0.75

print(f"Produtividade Média : {produtividade_media}\n Contagem de falhas: {contagem_falhas}\n Pagamento Final: {pagamento_final}")