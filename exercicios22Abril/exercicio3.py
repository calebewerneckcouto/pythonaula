"""Faça um Programa que verifique se uma letra digitada é "F"

ou
"M". Conforme a letra escrever:

1.

F - Feminino,
M - Masculino,

Outra letra qualquer - Sexo Inválido."""


valor = input('Digite uma letra: ')

if valor == 'f' or valor == 'F':
    print('Feminino') 
elif valor == 'm' or valor == 'M':    
     print('Masculino') 
else:
      print('Sexo Inválido') 