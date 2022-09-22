#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

p1 = input("Você possui irmãos? ")

if p1 == 'sim':
  print("Quantos?")
elif p1 == 'nao':
  print("Gostaria de ter?")