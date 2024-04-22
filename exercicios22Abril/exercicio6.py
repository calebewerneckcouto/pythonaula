"""Faça um programa que pergunte o preço de três
produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""

produto1 = int(input('Qual o valor do primeiro produto?'))
produto2 = int(input('Qual o valor do segundo produto?'))
produto3 = int(input('Qual o valor do terceiro produto?'))


numero = [produto1 , produto2,produto3]


print(min(numero))
  
