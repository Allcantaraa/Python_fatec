numero_total_questoes = int(input("Digite o numero total de questões do quiz: "))

pontuacao_bruta = 0
erros_consecutivos = 0

for i in range(numero_total_questoes) :
    pontuacao_obtida = float(input(f"Digite a pontuação obtida na {i} questão: "))

    if pontuacao_obtida == 10.0 :
        pontuacao_bruta += pontuacao_obtida
        erros_consecutivos = 0
    elif pontuacao_obtida < 5.0 :
        pontuacao_bruta += pontuacao_obtida
        erros_consecutivos += 1
    else :
        pontuacao_bruta += pontuacao_obtida
        erros_consecutivos = 0

if pontuacao_bruta > 40 and erros_consecutivos == 0 :
    print("Resultado Excelente! Bônus de 10 aplicado.")
    pontuacao_ajustada = pontuacao_bruta * 1.10
elif pontuacao_bruta < 20 or erros_consecutivos > 2 :
    print("Resultado Fraco. Penalidade de 15 aplicada.")
    pontuacao_ajustada = pontuacao_bruta * 0.85
else :
    print("Resultado Padrão. Sem bônus ou penalidade.")
    pontuacao_ajustada = pontuacao_bruta