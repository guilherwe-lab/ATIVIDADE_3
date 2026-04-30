  import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 5

print("jogo de adivinhação")
print(“Tente adivinhar o número de 1 e 100!")
print(f"Você tem {max_tentativas} tentativas.\n")
    
while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
  
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
      break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.\n")
    else:
        print("O número secreto é MENOR.\n")
       
    print(f"Tentativas restantes: {max_tentativas - tentativas}\n")
      
if palpite != numero_secreto:
    print("Fim de jogo! Você não acertou.")
    print(f"O número secreto era: {numero_secreto}")
JOGO DE ADIVINHAÇÃO
Tente adivinhar o número
