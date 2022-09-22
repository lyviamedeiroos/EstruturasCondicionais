#Faça um programa que verifique (usando if e else) se uma letra digitada é “F” ou “M”. Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido.

var = input("Informe M para Masculino ou F para Feminino: ")

if var == "M":
  print("Sexo masculino")
elif var == "F":
  print("Sexo feminino")
else: 
  print("Sexo inválido")