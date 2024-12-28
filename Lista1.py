#1)Faça um programa que peça dois números inteiros e imprima a soma desses dois números.

x = int(input('Escolha um número inteiro: '))
y = int(input('Escolha outro número inteiro: '))
print( x + y )


#2)Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

x = float(input('Metros: '))
print(x * 1000)


#3)Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

d = int(input('Dias: ' )) * 86400
h = int(input('Horas: ')) * 3600
m = int(input('Minutos: ')) * 60
s = int(input('Segundos: '))
print( d + h + m + s, 'segundos')


#4)Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

s = float(input('Salário: R$'))
a = float(input('Aumento: ')) / 100
x = s * a
y = s + x
print('O valor do aumento é',x)
print('O novo salário é R$',y)


#5)Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor de desconto e o preço a pagar.

m = float(input('Mercadoria: '))
d = float(input('Desconto: ')) / 100 
x = m * d
y = m - x
print('Valor do desconto: R$',x)
print('Novo preço da mercadoria: R$',y)


#6)Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem

d = int(input('Distância em km: '))
vm = int(input('Velocidade média em km/h: '))
t = d / vm
print('A duração total da viagem foi de',t,'horas')


#7)Converta uma temperatura digitada em Celsius para Fahrenheit. F=9*C/5+32
c = int(input('Celsius°: '))
f = 9*c / 5 + 32
print(c,'graus Celsius° equivalem a',f,'graus Fahrenheit°')


#8)Fala agora o contrário, de Fahrenheit para Celsius.
f = int(input('Fahrenheit°: '))
c = 5/9 * (f-32)
print(f,f'graus Fahrenheit° equivalem a {c:.0f} graus Celsius°')


#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

d = int(input('Quantidade de dias: '))
km = int(input('Distância percorrida em km: '))
vt = d*60 + km*0.15
print('O valor total a se pagar é R$',vt)


#10)Escreva um programa para a calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

c = int(input('Cigarros por dia: '))
a = int(input('Tempo que fumou em anos: '))
cgs = c * 365 * a
tmp= cgs*10 / 1440
print(f"Tempo perdido de vida é {tmp:.0f} dias")


#11)Sabendo que str() converte valores númericos para string, calcule quantos digitos há em 2 elevado a um milhão.

x = str(2**10000)
len(x)
print(len(x))
