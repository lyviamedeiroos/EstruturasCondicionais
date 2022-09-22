#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre o mais barato.

produto1 = int(input("Digite o preço do primeiro produto: "))
produto2 = int(input("Digite o preço do segundo produto: "))
produto3 = int(input("Digite o preço do terceiro produto: "))

produtoBarato = 0

if produto1 < produto2 and produto1 < produto3:
  produtoBarato = produto1
elif produto2 < produto1 and produto2 < produto3:
  produtoBarato = produto2
elif produto3 < produto1 and produto3 < produto2:
  produtoBarato = produto3

print("O produto mais barato é: " ,produtoBarato)