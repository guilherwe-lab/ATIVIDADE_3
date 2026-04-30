While True:
        Try:
               nota = float(input("Digite uma nota entre 0 e 10: "))
    
                if 0 <= nota <= 10:
                       print(f"Nota válida informada: {nota}")
                       break
        else:
                       print("Valor inválido! A nota deve estar entre 0 e 10.")
          
    except ValueError:
print("Entrada inválida! Por favor, digite um número."
