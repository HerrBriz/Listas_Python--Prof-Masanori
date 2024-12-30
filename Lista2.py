#1Faça um programa que peça os três lado de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

l1 = int(input("Primeiro lado do triângulo: "))
l2 = int(input("Segundo lado do triângulo: "))
l3 = int(input("Terceiro lado do triângulo: "))

if l1+l2>l3 or l1+l3>l2 or l2+l3>l1:
    print("É um triângulo.")

    if l1==l2==l3:
        print("É um triângulo equilátero.")
    
    if l1==l2 or l1==l3 or l2==l3:
        print("É um triângulo isósceles.")
     
    if l1!=l2!=l3!=l1:
        print("É um triângulo escaleno.") 



#2Determine se um ano pe bissexto. Verifique no Google como fazer isso.
        
ano = int(input("Ano: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("É ano bissexto.")
else:
    print("Não é um ano bissexto.")



#3João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido oeli regulamento de pesca do estado de São Paulo(50 quilos) deve pagar uma multa de R$4,00 por quilo excedente. João precisa que você  faça um programa que leia a variável peso (peso de peixes) e verifiqye se há excesso. Se houver, gravar na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o contéudo zero.
    
peso = float(input("Peso: "))
if peso > 50:
    print(f'Excesso de {peso-50:.2f} kg')
    print(f"Multa de R${(peso-50)*4:.2f}")
else:
    print(0)


   
#4Faça um programa que peça três números e mostre o maior deles.
x = int(input("Escolha um número: "))
y = int(input("Escolha um número: "))
z = int(input("Escolha um número: "))

if x>=y and x>=z:
    print(f'O número {x} é o maior')
elif y>=z:
    print(f'O número {y} é o maior')
else:
    print(f'O número {z} é o maior')

 
#5Faça um programa que peça três números e mostre o maior e o menor deles.
    
x = int(input("Escolha um número: "))
y = int(input("Escolha um número: "))
z = int(input("Escolha um número: "))

if x>=y and x>=z:
    print(f'O número {x} é o maior')
elif y>=z:
    print(f'O número {y} é o maior')
else:
    print(f'O número {z} é o maior')

if x<=y and x<=z:
    print(f"O número {x} é o menor")
elif y<=z:
    print(f"O número {y} é o menor")
else:
    print(f"O número {z} é o menor")


    

 
#6Faça um programa que pergunte quanto voçê ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o toral do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que o Salário Bruto - Desconto = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo:
#a. +Salário Bruto: R$
#b. -IR(11%): R$
#c. -INSS(8%): R$
#d. Sindicato: R$
#e. = Salário Líquido: R$
    
sh = float(input("Valor pago por hora: "))
ht = int(input("Horas trabalhadas por mês: "))
sl = sh * ht
print(f'Salário Bruto: R${sl}')
print(f'IR: R${sl*0.11}')
print(f'INSS: R${sl*0.08}')
print(f'Sindicato: R${sl*0.05}')
print(f'Salário Líquido: R${sl - ((sl*0.11)+(sl*0.08)+(sl*0.05))}')


#7Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de um 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidades de latas se tinta a serem compradas e o preço total. Obs.: somente são vendidos um número inteiro de latas.

metros = int(input("Tamanho da área(m²): "))
latas = 54
if metros % latas == 0:
    print(f"Deve ser compradas {metros / latas:.0f} latas")
    preço = metros / latas
    print(f"Custará R${preço*80:.2f} Reais")
if metros % latas != 0:
    print(f"Deve ser compradas {metros / latas + 1:.0f} latas")
    preço = int(metros / latas)  + 1
    print(f"Custará R${preço*80:.2f} Reais")
