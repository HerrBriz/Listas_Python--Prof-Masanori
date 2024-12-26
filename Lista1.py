#1)
x = int(input('Escolha um número inteiro: '))
y = int(input('Escolha outro número inteiro: '))
print( x + y )


#2)
x = float(input('Metros: '))
print(x * 1000)


#3)
d = int(input('Dias: ' )) * 86400
h = int(input('Horas: ')) * 3600
m = int(input('Minutos: ')) * 60
s = int(input('Segundos: '))
print( d + h + m + s, 'segundos')


#4)
s = float(input('Salário: R$'))
a = float(input('Aumento: ')) / 100
x = s * a
y = s + x
print('O valor do aumento é',x)
print('O novo salário é R$',y)


#5)
m = float(input('Mercadoria: '))
d = float(input('Desconto: ')) / 100 
x = m * d
y = m - x
print('Valor do desconto: R$',x)
print('Novo preço da mercadoria: R$',y)


#6)
d = int(input('Distância em km: '))
vm = int(input('Velocidade média em km/h: '))
t = d / vm
print('A duração total da viagem foi de',t,'horas')


#7)
c = int(input('Celsius°: '))
f = 9*c / 5 + 32
print(c,'graus Celsius° equivalem a',f,'graus Fahrenheit°')


#8)
f = int(input('Fahrenheit°: '))
c = 5/9 * (f-32)
print(f,f'graus Fahrenheit° equivalem a {c:.0f} graus Celsius°')


#9)
d = int(input('Quantidade de dias: '))
km = int(input('Distância percorrida em km: '))
vt = d*60 + km*0.15
print('O valor total a se pagar é R$',vt)


#10)
c = int(input('Cigarros por dia: '))
a = int(input('Tempo que fumou em anos: '))
cgs = c * 365 * a
tmp= cgs*10 / 1440
print(f"Tempo perdido de vida é {tmp:.0f} dias")


#11)
x = str(2**10000)
len(x)
print(len(x))
