nota = float(input("Digite uma nota entre 0 e 10: "))
 
while nota < 0 or nota > 10:

  print("Valor inválido! A nota deve estar entre 0 e 10.")

  nota = float(input("Digite novamente: "))

print(f"Nota válida informada: {nota}")
