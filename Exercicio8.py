#Faça um programa que leia três números, verifique (usando if e else) e mostre o maior e o menor deles;

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

maiorNum = 0
menorNum = 0
if numero1 > numero2 and numero1 > numero3:
  maiorNum = numero1
elif numero2 > numero1 and numero2 > numero3:
  maiorNum = numero2
elif numero3 > numero1 and numero3 > numero2:
  maiorNum = numero3

if numero1 < numero2 and numero1 < numero3:
  menorNum = numero1
elif numero2 < numero1 and numero2 < numero3:
  menorNum = numero2
elif numero3 < numero1 and numero3 < numero2:
  menorNum = numero3
print("O maior número é: ",maior)
print("O menor número é: ",menor)
