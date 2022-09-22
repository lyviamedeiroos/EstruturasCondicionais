#Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de multiplicação ou de divisão e que, a partir desta escolha, mostre o resultado na tela.

numero1 = int(input("Primeiro número: "))
numero2 = int(input("Segundo número: "))

op = input("Informe a operação que você deseja realizar (* ou /):")

if op == "*":
  resultado = numero1 * numero2
elif op == "/":
  resultado = numero1 / numero2
  resultado = 0
print("Resultado", resultado)