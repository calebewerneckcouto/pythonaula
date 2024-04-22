"""Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:
Salário bruto
Quanto pagou ao INSS.
Quanto pagou ao sindicato.
O salário líquido.

Calcule os descontos e o salário líquido, conforme a tabela abaixo:
Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$"""

ganhaporhoras = float(input('Quanto vc ganha por hora?'))

horastrabalhadas = float(input('Quantas horas vc trabalhou no mes?'))

totalsalario =  ganhaporhoras * horastrabalhadas

impostoderenda =(totalsalario*11)/100
inss =(totalsalario*8)/100
sindicato = (totalsalario * 5)/100

salarioliquido = totalsalario - (impostoderenda + inss + sindicato)

print(f'Salário Bruto : R${totalsalario}')
print(f'IR (11%) : R${impostoderenda}')
print(f'INSS (8%) : R${inss}')
print(f'Sindicato ( 5%) : R${sindicato}')
print(f'Salário Liquido é : R${salarioliquido}')


