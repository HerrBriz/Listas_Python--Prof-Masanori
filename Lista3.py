#1Faça um programa que peça uma nota, entre 0 e 10. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Insira uma nota 0 até 10: "))
while nota<0 or nota>10:
    print("Valor inválido!")
    nota = float(input("Insira uma nota 0 até 10: "))
print("Nota válida")


#2Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Nome do usuário: ")
senha = input("Senha: ")
while nome == senha:
    senha = input("Senha inválida. Insira senha:")
print("Senha aceita!!!")
 

#3Supondo que a população de um país A seja de ordem 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja de 200000 habitantes com uma taxa de crescimento de 1.5% . Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população de B, mantidas as taxas de crescimento.

a = 80000
b = 200000
ano = 0
while b > a:
    a = a + a*0.03
    b = b + b*0.015
    ano = ano + 1
print(f"Durará {ano} anos até que a populção de A ultratapasse B ")


#4A sequência d Fibonacci é a seguinte:1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua refra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.

n = int(input("Digite um número: "))

a, b = 1, 1
k = 1

while k <= n-1:
    a, b = b, a + b
    k = k + 1

print(b)


#5Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
p1 = int(input("Número 1: "))
p2 = int(input("Número 2: "))

while p1%p2 != 0:
    p1, p2 = p2, p1%p2
    
print(f"mdc = {p2}")
    
