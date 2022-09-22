#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: “Telefonou para a vítima? “ “Esteve no local do crime?” “Mora perto da vítima? “ “Devia para a vítima? “ “Já trabalhou com a vítima? “ O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.

p1 = input("Você telefonou para a vítima? ")
p2 = input("Você esteve no local do crime? ")
p3 = input("Você mora perto da vítima? ")
p4 = input("Você devia para a vítima? ")
p5 = input("Você já trabalhou com a vítima? ")

cont = 0

if p1 == 'sim':
  cont+=1
if p2 == 'sim':
  cont+=1
if p3 == 'sim':
  cont+=1
if p4 == 'sim':
  cont+=1
if p5 == 'sim':
  cont +=1

if cont == 2:
  print("Suspeito")
elif cont > 2 <=4:
  print("Cumplice")
elif cont > 4:
  print("Assassino")
else: 
  print("inocente")
