# lista = [ i for i in range(1,11)]

# lista_pares = [ i for i in lista if i % 2 == 0 ]

# print(lista_pares)

mensagem = ""

print("--- Repetidor Interativo ---")

print("Digite 'sair' a qualquer momento para encerrar o programa.")

while mensagem != "sair":
    mensagem = input("Digite uma mensagem: ").lower()
    if mensagem != "sair":
        print(f"Você digitou: {mensagem}")

print("\nPrograma encerrado. Até logo!")