#1Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.

import random
L = random.sample(range(100), 10)
maior = L[0]
menor = L[0]
for i in L:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i
print(L)
print(f'O maior é {maior} e menor é {menor}')



#2Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random
N = random.sample(range(100), 20)
par = []
impar = []
for i in N:
    if i%2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(N)
print(f"Os números pares são {par}")
print(f"Os números impares são {impar}")



#3Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.

import random
v1 = random.sample(range(100), 10)
v2 = random.sample(range(100), 10)
v3 = zip(v1, v2)
print(f'Vetor 1: {list(v1)}')
print(f'Vetor 2: {list(v2)}')
print(f'Vetor 3: {list(v3)}')


#4Seja o statement sobre diversidade: "The Python Software Foudation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other to live up these principles. We want our community to be more diverse: whoever you are, anfd whatever your background, we welcome you.". Gere uma lista de palavras este texto com split(), a seguir crie uma lista com palavras que começam ou terminam com uma das letras "python". Imprima a lista resultante. Não se esqueça de remover antes antes os caracteres especiais e cuidado com maiscúlas e minuscúlas.

txt = '''The Python Software Foundation and the global Python community welcome and encourage participation 
by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help
each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever
your background, we welcome you'''
txt = txt.replace(',','').replace('.','').replace(':','')
txt = txt.lower()
txt = txt.split()
for x in txt:
    if x[0] in 'python' or x[-1] in 'python':
        print(x)



#5Seja o mesmo texto acima "splitado". Calcule quantas palavras possuem uma das letras "python" e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
                
txt = '''The Python Software Foundation and the global Python community welcome and encourage participation 
by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help
each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever
your background, we welcome you'''.lower()

def pythonisch(wort):
    for letra in wort:
        if letra in 'python':
            return True
    return False

res = []
for p in txt.split():
    if pythonisch(p) and len(p) > 4:
        res.append(p)

print(len(res))
