#Escreva um programa que pergunte o dia, mês e ano do aniversário de uma pessoa e diga se a data é válida ou não. Caso não seja, diga o motivo.

dia = int(input("Informe o dia do seu aniversário: "))
mes = int(input("Informe o mes do seu aniversário: "))
ano = int(input("Informe o ano do seu aniversário: "))

if dia > 0 and dia < 32 and mes > 0 and mes < 13 and ano > 0 and ano < 2023:
  print ("data válida")
else:
  print ("data inválida")