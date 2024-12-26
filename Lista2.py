#1
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



#2
ano = int(input("Ano: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("É ano bissexto.")
else:
    print("Não é um ano bissexto.")



#3
peso = float(input("Peso: "))
if peso > 50:
    print(f'Excesso de {peso-50:.2f} kg')
    print(f"Multa de R${(peso-50)*4:.2f}")
else:
    print(0)


   
#4
x = int(input("Escolha um número: "))
y = int(input("Escolha um número: "))
z = int(input("Escolha um número: "))

if x>=y and x>=z:
    print(f'O número {x} é o maior')
elif y>=z:
    print(f'O número {y} é o maior')
else:
    print(f'O número {z} é o maior')

 
#5
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


    

 
#6   
sh = float(input("Valor pago por hora: "))
ht = int(input("Horas trabalhadas por mês: "))
sl = sh * ht
print(f'O salário total é R${sl:.2f}')

descontos =((sl*0.11)+(sl*0.08)+(sl*0.05))

print(f'Salário Líquido: R${sl-descontos:.2f}')



#7
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
