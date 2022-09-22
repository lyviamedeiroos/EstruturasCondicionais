#  Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno. Imprima a mensagem “Bom dia!” ou "Boa Tarde" ou “Boa Noite” ou “Valor inválido”, conforme o caso.

var = input("Qual turno você estuda? M - Matutino, V - Verspertino, N - Noturno: ")

if var == "m":
  print("Bom dia")
elif var == "v":
  print("Boa tarde")
elif var == "n":
  print("Boa noite")
else:
  print("Valor invalido")
