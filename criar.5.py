While True:
    try:
        # 1. Entrada de dados
        nota = float(input("Digite uma nota entre 0 e 10: "))

        # 2. Verificação da regra (se a nota é válida)
        if 0 <= nota <= 10:
            print(f"Nota válida informada: {nota}")
            break  # Sai do laço se tudo estiver correto
        
        # 3. Se a nota for número, mas estiver fora do intervalo (ex: 11)
        print("Valor inválido! A nota deve estar entre 0 e 10.")

    except ValueError:
        # 4. Se o usuário digitar letras ou símbolos em vez de números
        print("Entrada inválida! Por favor, digite apenas números.")
