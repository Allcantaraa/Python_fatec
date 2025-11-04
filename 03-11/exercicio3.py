SENHA_CORRETA = "python123"
tentativas_erradas = 0
senha_digitada = ""  # Inicializa a variável para garantir que o loop comece

print("\n--- Sistema de Login ---")

while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada == SENHA_CORRETA:
        print(f"\nSenha válida! Acesso concedido.")       
    else:
        tentativas_erradas += 1
        print("Senha incorreta. Tente novamente.")

# O programa termina aqui após o while
print ("Total de entradas erradas", tentativas_erradas)

#RESPOSTA: é porque o usuário ira digitar. Mas não podemos inicilializar ela dentro do loop porque o loop só inicia se a variável existir.