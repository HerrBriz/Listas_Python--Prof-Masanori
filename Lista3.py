#1
nota = float(input("Insira uma nota 0 até 10: "))
while nota<0 or nota>10:
    print("Valor inválido!")
    nota = float(input("Insira uma nota 0 até 10: "))
print("Nota válida")


#2
nome = input("Nome do usuário: ")
senha = input("Senha: ")
while nome == senha:
    senha = input("Senha inválida. Insira senha:")
print("Senha aceita!!!")
 

#3
a = 80000
b = 200000
ano = 0
while b > a:
    a = a + a*0.03
    b = b + b*0.015
    ano = ano + 1
print(f"Durará {ano} anos até que a populção de A ultratapasse B ")


#4
n = int(input("Digite um número: "))

a, b = 1, 1
k = 1

while k <= n-1:
    a, b = b, a + b
    k = k + 1

print(b)


#5
p1 = int(input("Número 1: "))
p2 = int(input("Número 2: "))

while p1%p2 != 0:
    p1, p2 = p2, p1%p2
    
print(f"mdc = {p2}")
    
