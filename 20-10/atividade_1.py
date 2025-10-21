num_pos = int(input("Número: "))
soma_dos_quadrados = 0

for i in range(num_pos) :
    quadrado = i * i

    if i % 3 == 0 :
        print(f"{i} é multiplo de 3")
    elif i % 2 == 0 :
        soma_dos_quadrados += quadrado
        print(f"{i} é Par. Quadrado Acumulado")
    else :
        print(f"{i} é Impar. Ignorado")

print(f"Valor final dos quadrados: {soma_dos_quadrados}")