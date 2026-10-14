#Crie um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve contar quantas vezes o valor x aparece dentro da lista e retornar a quantidade de ocorrências.
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre 1 e 30, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar a quantidade de ocorrências no final.

from random import randint

def valor(lis, x):
    quant = 0
    for i in range(len(lis)):
        if lis[i] == x:
            quant += 1
    return quant


def main():
    lis = [randint(1, 30)for _ in range (15)]
    print(lis)

    x = int(input('\nDigite o valor a ser procurado: '))

    oc = valor(lis, x)

    print(f'\nA quantidade de vezes que valor {x} apareceu foi {oc}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve identificar todos os elementos da lista iguais a x, somar esses valores e retornar o resultado da soma.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 20, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar a soma das ocorrências encontradas no final.

from random import randint

def soma(lis, x):
    soma = 0
    for i in range(len(lis)):
        if lis[i] == x:
            soma += 1

    return soma


def main():
    lis = [randint(1,20)for _ in range(20)]

    print(lis)

    x = int(input('\n Insira um valor inteiro a ser somado: '))

    so = soma(lis, x)

    print(f'\n A soma das vezes que o {x} apareceu na lista foi {so}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros (1 parâmetro). A função deve procurar todos os números pares presentes na lista e retornar uma nova lista contendo os índices em que esses números aparecem.
#O programa principal deve gerar e mostrar uma lista com 18 valores inteiros aleatórios entre 1 e 100, chamar a função passando a lista como parâmetro e mostrar as posições dos números pares encontrados.

from random import randint

def inteiro(lis):

    pares = []

    for i in range(len(lis)):
        if lis[i] %2 == 0 :
            pares.append(i)

    return pares

def main():
    lis = [randint(1,100) for _ in range(18)]

    p = inteiro(lis)

    print(f'\n Os valores pares aparecem nos indices {p}')

    print(lis)
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve procurar todos os elementos da lista que sejam maiores que x e retornar uma lista contendo os índices desses elementos.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 100, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar as posições dos elementos maiores que x no final.

from random import randint

def func(lis, x):

    maiores = []

    for i in range(len(lis)):
        if lis[i] > x:
            maiores.append(i)

    return maiores


def main():

    lis = [randint(1,100)for _ in range(20)]

    print(lis)

    x = int(input('\n Digite um valor:'))

    p = func(lis, x)

    print(f'\n Os indices que os valores da lista são maiores que {x} são: {p}')

    print(lis)
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve procurar o valor x dentro da lista e retornar uma lista contendo o índice da primeira ocorrência e o índice da última ocorrência desse valor.
#Caso o valor x não esteja presente na lista, a função deve retornar uma lista vazia.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 15, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar o resultado da busca no final.

from random import randint

def func(lis, x):

    ind = []

    for i in range(len(lis)):
        if lis[i] == x:
            ind.append(i)
            break

    for i in range(len(lis) - 1, -1, -1):
        if lis[i] == x:
            ind.append(i)
            break

    return ind

def main():

    lis = [randint(1, 15)for _ in range(20)]

    print(lis)

    x = int(input('\n Digite um valor inteiro: '))

    p = func(lis, x)

    print(f'\n Resultado da busca pelo {x} foi de {p}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O menor e o maior valor da lista.
2. A média aritmética dos valores positivos da lista.
3. A quantidade de valores múltiplos de 5.
4. A soma dos valores pares da lista.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -30 e 30, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    med = []

    for i in range(len(lis)):
        if lis[i] >= 0:
            med.append(i)

    media = len(med)/ sum(med)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %5 == 0:
            quant =+ 1

    pares =[]

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            pares.append(i)

    soma = sum(pares)

    return maior, menor, media, soma

def main():

    lis = [randint(-30, 30)for _ in range(20)]

    print(lis)

    maior, menor, media, soma = calculos(lis)

    print(f'Maior = {maior}')
    print(f'Menor = {menor}')
    print(f'Media positivos = {media}')
    print(f'Soma dos pares = {soma}')
main()



#Crie um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O maior valor par e o menor valor ímpar da lista.
2. A média aritmética dos valores pares da lista.
3. A quantidade de valores ímpares.
4. A diferença entre o maior e o menor valor da lista.
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -20 e 50, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    par = []
    imp = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            par.append(i)
        else:
            imp.append(i)

    mp = max(par)
    mi = min(imp)

    media = len(par) / sum(par)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            quant += 1

    dif = mp - mi

    return mp, mi, media, quant, dif

def main():

    lis = [randint(-20, 50)for _ in range(15)]

    print(lis)

    mp, mi, media, quant, dif = calculos(lis)

    print(f'Maior numero par: {mp}')
    print(f'Menor numero impar: {mi}')
    print(f'Media dos numeros pares: {media}')
    print(f'Diferença entre maior e menor na lista: {dif}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O menor e o maior valor da lista.
2. A quantidade de valores múltiplos de 3.
3. A soma dos valores múltiplos de 5.
4. A média aritmética dos valores negativos da lista.
#O programa principal deve gerar e mostrar uma lista com 25 valores inteiros aleatórios entre -40 e 40, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            quant += 1

    mult = []

    for i in range(len(lis)):
        if lis[i] %5 == 0:
            mult.append(i)

    soma = sum(mult)

    vn = []

    for i in range(len(lis)):
        if lis[i] < 0:
            vn.append(i)

    media = len(vn) / sum(vn)

    return maior, menor, quant, soma, media

def main():

    lis = [randint(-40, 40)for _ in range(25)]

    print(lis)

    maior, menor, quant, soma, media = calculos(lis)

    print(f'Maior valor da lista: {maior}')
    print(f'Menor valor da lista: {maior}')
    print(f'Quantidade multiplos de 3: {quant}')
    print(f'Soma dos multiplos de 5: {soma}')
    print(f'Media dos valores negativos: {media}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. A quantidade de valores positivos, negativos e iguais a zero.
2. A soma de todos os valores positivos da lista.
3. A média aritmética dos valores negativos da lista.
4. A diferença entre o maior valor positivo e o menor valor negativo.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -50 e 50, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    quantp = 0
    quantn = 0
    ig = 0

    for i in range(len(lis)):
        if lis[i] > 0:
            quantp += 1
        if lis[i] < 0:
            quantn += 1
        if lis[i] == 0:
            ig += 1

    vp = []

    for i in range(len(lis)):
        if lis[i] > 0:
            vp.append(i)

    soma = sum(vp)

    vn = []

    for i in range(len(lis)):
        if lis[i] < 0:
            vn.append(i)

    media = len(vn) / sum(vn)

    posi = []
    neg = []

    for i in range(len(lis)):
        if lis[i] > 0:
            posi.append(i)
        else:
            neg.append(i)

    mp = max(posi)
    mn = min(neg)

    dif = mp - mn

    return quantp, quantn, ig, soma, media, dif

def main():

    lis = [randint(-50, 50)for _ in range(20)]

    print(lis)

    quantp, quantn, ig, soma, media, dif = calculos(lis)

    print(f'Quantidade de numeros positivos: {quantp}')
    print(f'Quantidade de numeros negativos: {quantn}')
    print(f'Quantidade de numeros iguais a 0: {ig}')
    print(f'Soma dos numeros positivos: {soma}')
    print(f'Media dos valores negativos: {media}')
    print(f'Diferença entre o maior positivo e menor negativo: {dif}')
main()

#Crie um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O segundo maior valor da lista.
2. A quantidade de valores divisíveis por 2 e por 3 ao mesmo tempo.
3. A média aritmética dos valores maiores que 10.
4. A diferença entre o maior valor par e o menor valor par da lista.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 100, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    maior = lis[0]
    segundo = None

    for i in range(len(lis)):
        if lis[i] > maior:
            segundo = maior
            maior = lis[i]
        elif lis[i] != maior:
            if segundo == None or lis[i] > segundo:
                segundo = lis[i]

    quant = 0
    for i in range(len(lis)):
        if lis[i] %2 == 0 and lis[i] %3 == 0:
            quant += 1

    md = []

    for i in range(len(lis)):
        if lis[i] > 10:
            md.append(i)

    media = len(md) / sum(md)

    pares = []

    for i in range(len(lis)):
        if lis[i] % 2 == 0:
            pares.append(lis[i])

    maior = max(pares)
    menor = min(pares)

    dif = maior - menor

    return segundo, quant, media, dif

def main():

    lis = [randint(1,100) for _ in range(20)]

    print(lis)

    segundo, quant, media, dif = calculos(lis)

    print(f'O segundo maior valor da lista é: {segundo}')
    print(f'Quantidade de valores divisiveis por 2 e 3: {quant}')
    print(f'Media dos valores maiores que 10: {media}')
    print(f'Diferença entre o maior e menor valor par: {dif}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve procurar pelo valor x dentro da lista e retornar a quantidade de vezes que esse valor aparece.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 100, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar a quantidade de ocorrências do valor procurado no final.

from random import randint 

def param(lis, x):

    quant = 0

    for i in range(len(lis)):
        if lis[i] == x:
            quant += 1 

    return quant

def main():

    lis = [randint(1,100)for _ in range(20)]

    print(lis)

    x = int(input('Digite o valor de X:'))

    p = param(lis,x)

    print(f'A quantidade de vezes que o {x} apareceu na lista foi de: {p}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro. A função deve retornar uma lista contendo as posições (índices) de todos os valores pares encontrados na lista. 
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre 1 e 50, chamar a função passando a lista como parâmetro e mostrar as posições dos valores pares no final.

from random import randint 

def pares(lis):

    pares = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            pares.append(i)

    return pares



def main():

    lis = [randint(1, 50)for _ in range(15)]

    print(lis)

    p = pares(lis)

    print(f'A posição em que os numeros pares aparecem na lista é {p}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve retornar uma nova lista contendo apenas os valores maiores que x, mantendo a ordem em que aparecem na lista original. 
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 100, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar a nova lista no final.

from random import randint

def param(lis, x):

    novalis = []

    for i in range(len(lis)):
        if lis[i] > x:
            novalis.append(i)

    return novalis


def main():

    lis = [randint(1,100)for _ in range(20)]

    print(lis)

    x = int(input('Digite o valor de X:'))

    p = param(lis, x)

    print(f'Os valores que são maiores que {x} são: {p}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro positivo diferente de zero (2 parâmetros). A função deve retornar uma lista contendo as posições (índices) de todos os valores da lista que são múltiplos de x. 
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 100, ler um valor inteiro positivo fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar as posições encontradas no final.

from random import randint

def param(lis, x):

    novalis = []

    for i in range(len(lis)):
        if lis[i] %x == 0:
            novalis.append(i)

    return novalis

def main():

    lis = [randint(1, 100)for _ in range(20)]
    print(lis)

    x = (int(input('Digite o valor a ser procurado: ')))

    p = param(lis, x)

    print(f' Os valores que são multiplos de {x} estão nos indices: {p}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros e um valor x inteiro qualquer (2 parâmetros). A função deve retornar uma lista contendo todos os valores da lista original que sejam diferentes de x, mantendo a ordem em que aparecem. 
#O programa principal deve gerar e mostrar uma lista com 25 valores inteiros aleatórios entre 1 e 50, ler um valor inteiro fornecido pelo usuário e chamar a função passando a lista e o valor x como parâmetros. Mostrar a lista resultante após a remoção lógica dos valores iguais a x, sem modificar a lista original.

from random import randint 

def param(lis, x):

    lis1 = []

    for i in range(len(lis)):
        if lis[i] != x:
            lis1.append(i)

    return lis1

def main():

    lis = [randint(1,50)for _ in range(25)]
    print(lis)

    x = int(input('Digite o valor de X: '))

    p = param(lis, x)

    print(f'A nova lista com numeros diferentes de {x} é : {p}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
- O menor e o maior valor par da lista.
- A média aritmética dos valores ímpares da lista.
- A quantidade de valores negativos.
- A diferença entre o maior valor positivo e o menor valor negativo.
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -30 e 30, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    pares = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            pares.append(i)

    mp = max(pares)
    mnp = min(pares)

    imp = []

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            imp.append(i)

    media = len(imp) / sum(imp)

    quant = 0 

    for i in range(len(lis)):
        if lis[i] < 0:
            quant += 1

    positivos = []
    negativos = []

    for i in range(len(lis)):
        if lis[i] > 0:
            positivos.append(i)
        else: 
            negativos.append(i)
    
    maiorp = max(positivos)
    menorn = min(negativos)

    dif = maiorp - menorn

    return mp, mnp, media, quant, dif

def main():

    lis = [ randint(-30, 30)for _ in range(15)]
    print(lis)

    mp, mnp, media, quant, dif = calculos(lis)

    print(f'O maior numero par: {mp}')
    print(f'O menor numero par: {mnp}')
    print(f'A media entre os numeros impares: {media}')
    print(f'Quantidade de valores negativos: {quant}')
    print(f'Diferença entre o menor positivo e menor negativo: {dif}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
- O menor e o maior valor da lista.
- A quantidade de valores múltiplos de 3.
- A média aritmética dos valores positivos da lista.
- A soma dos valores pares da lista.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -25 e 50, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint 

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0 

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            quant += 1 

    positivos = []

    for i in range(len(lis)):
        if lis[i] > 0:
            positivos.append(i)

    media = len(positivos) / sum(positivos) 

    pares = []

    for i in range(len(lis)):
        if lis[i] > 0:
            pares.append(i)

    soma = sum(pares)

    return maior, menor, quant, media, soma 

def main():

    lis = [randint(-25, 50)for _ in range(20)]
    print(lis)

    maior, menor, quant, media, soma = calculos(lis)

    print(f'O maior valor da lista é: {maior}')
    print(f'O menor valor da lista é: {menor}')
    print(f'A quantidade de multiplos de 3: {quant}')
    print(f'A media dos valores positivos: {media}')
    print(f'Soma dos valores pares: {soma}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
- O menor e o maior valor negativo da lista.
- A quantidade de valores positivos.
- A média aritmética dos valores negativos da lista.
- A diferença entre o maior valor par e o menor valor ímpar da lista.
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -40 e 40, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint 

def calculos(lis):

    negativos = []

    for i in range(len(lis)):
        if lis[i] < 0:
            negativos.append(i)

    maior = max(negativos)
    menor = min(negativos)

    quant = 0 

    for i in range(len(lis)):
        if lis[i] > 0:
            quant += 1 

    media = len(negativos) / sum(negativos)

    pares = []
    imp = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            pares.append(i)
        else:
            imp.append(i)
    
    mp = max(pares)
    mi = min(imp)

    dif = mp - mi 

    return maior, menor, quant, media, dif

def main():

    lis = [randint(-40, 40)for _ in range(15)]
    print(lis)

    maior, menor, quant, media, dif = calculos(lis)

    print(f'O maior valor negativo da lista é: {maior}')
    print(f'O menor valor negativo da lista é: {menor}')
    print(f'A quantidade de valores positivos: {quant}')
    print(f'A media dos valores negativos: {media}')
    print(f'A difereça do maior par e menor impar: {dif}')
main()

#Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
- O menor e o maior valor da lista.
- A quantidade de valores pares e positivos.
- A média aritmética dos valores múltiplos de 5.
- A diferença entre o maior valor ímpar e o menor valor par.
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -50 e 50, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %2 == 0 and lis[i] > 0:
            quant += 1 

    mult = []

    for i in range(len(lis)):
        if lis[i] %5 == 0:
            mult.append(i)

    media = len(mult) / sum(mult)

    imp = []
    par = []

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            imp.append(i)
        else:
            par.append(i)

    maiori = max(imp)
    menorp = min(par)

    dif = maiori - menorp

    return maior, menor, quant, media, dif

def main():

    lis = [randint(-50, 50)for _ in range(20)]
    print(lis)

    maior, menor, quant, media, dif = calculos(lis)

    print(f'O maior valor da lista é: {maior}')
    print(f'O menor valor da lista é: {menor}')
    print(f'A quantidade de valores pares e positivos: {quant}')
    print(f'A media dos valores multiplos de 5: {media}')
    print(f'A difereça do maior par e menor impar: {dif}')  
main()

#1. Crie um programa com uma função que recebe uma lista de números inteiros e um número inteiro $x$ (2 parâmetros). A função deve calcular e retornar a quantidade de vezes que o valor $x$ aparece dentro da lista. 
#O programa principal deve preencher uma lista com 15 números inteiros aleatórios entre 10 e 30, solicitar que o usuário digite um valor inteiro para busca, chamar a função passando ambos os argumentos e exibir o total de ocorrências encontradas.

from random import randint

def busca(lis, x):

    quant = 0

    for i in range(len(lis)):
        if lis[i] == x:
            quant += 1 

    return quant

def main():

    lis = [randint(10, 30)for _ in range(15)]
    print(lis)

    x = int(input('\nDigite o valor x de busca:'))

    p = busca(lis, x)

    print(f'A quantidade de vezes que {x} apareceu na lista foi de {p}')
main()

#2. Criar um programa com uma função que recebe uma lista com valores inteiros e dois valores inteiros a e b como parâmetros (3 parâmetros). A função deve retornar uma lista contendo as posições (índices) dos valores que estão entre a e b, incluindo os próprios limites.
# O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -30 e 70, ler dois valores inteiros fornecidos pelo usuário e chamar a função passando a lista e os dois valores como parâmetros. Mostrar as posições encontradas no final.

from random import randint

def busca(lis, a, b):

    novalis = []

    for i in range(len(lis)):
        if a <= lis[i] <= b:
            novalis.append(i)

    return novalis

def main():

    lis = [randint(-30, 70)for _ in range(20)]
    print(lis)

    a = int(input('\n Digite o valor de a: '))
    b = int(input('\n Digite o valor de b: '))

    p = busca(lis, a, b)

    print(f'\n Os indices dos valores que estão entre {a} e {b} são: {p}')
main()

# 3. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro. A função deve retornar uma lista contendo as posições (índices) dos valores que aparecem apenas uma vez na lista original. 
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 30, chamar a função passando a lista como parâmetro e mostrar as posições dos valores que não se repetem no final.

from random import randint

def unica(lis):

    newlis = []

    for i in range(len(lis)):
        if lis.count(lis[i]) == 1:
            newlis.append(i)

    return newlis

def main():

    lis = [randint(1, 30)for _ in range(20)]
    print(lis)

    p = unica(lis)

    print(f'O indice dos valores que aparecem somente uma vez na lista é : {p}')
main()

#4. Criar um programa com uma função que recebe uma lista com valores inteiros e um valor inteiro x como parâmetros (2 parâmetros). A função deve retornar uma lista contendo as posições (índices) dos valores que aparecem antes da primeira ocorrência de x na lista. Caso x não exista na lista, a função deve retornar uma lista vazia. 
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 50, ler um valor inteiro fornecido pelo usuário, chamar a função passando a lista e x como parâmetros e mostrar o resultado no final.

from random import randint

def func(lis, x):

    indices = []

    for i in range(len(lis)):
        if lis[i] == x:
            break
        indices.append(i)

    return indices

def main():

    lis = [randint(1, 50)for _ in range(20)]
    print(lis)

    x = int(input('\n Digite o valor referencia de X: '))

    p = func(lis, x)

    print(f'Os indices dos valores que aparecem até {x} são: {p}')
main()

#5. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro. A função deve retornar uma lista contendo as posições (índices) dos elementos que possuem o mesmo valor que o elemento imediatamente anterior. O primeiro elemento da lista não deve ser considerado, pois não possui um elemento anterior. 
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre 1 e 10, chamar a função passando a lista como parâmetro e mostrar as posições encontradas no final.

from random import randint

def busca(lis):

    indices = []

    for i in range(1, len(lis)):
        if lis[i] == lis[i - 1]:
            indices.append(i)

    return indices

def main():

    lis = [randint(1,10)for _ in range(20)]
    print(lis)

    p = busca(lis)

    print(f'A lista de indeces dos valores que são iguais ao seus sucessores é: {p}')
main()

#1.Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O menor e o maior valor da lista.
2. A quantidade de valores positivos.
3. A média aritmética dos valores pares.
4. A diferença entre o maior valor ímpar e o menor valor par (maior_impar - menor_par).
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -30 e 30, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint 

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0
    for i in range(len(lis)):
        if lis[i] > 0:
            quant += 1 

    pares = []
    imp = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            pares.append(i)
        else:
            imp.append(i)

    media = len(pares) / sum(pares)

    maiori = max(imp)
    menorp = min(pares)

    dif = maiori - menorp

    return maior, menor, media, dif

def main():

    lis =[randint(-30, 30)for _ in range(15)]
    print(lis)

    maior, menor, media, dif = calculos(lis)

    print(f'O maior valor da lista é: {maior}')
    print(f'O menor valor da lista é: {menor}')
    print(f'A media dos valores pares: {media}')
    print(f'A diferencia do maior impar e menor impar: {dif}')
main()

#2. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. A quantidade de valores negativos.
2. A soma dos valores positivos.
3. O menor valor negativo e o maior valor positivo.
4. A diferença entre o maior valor positivo e o menor valor negativo (maior_positivo - menor_negativo).
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -50 e 50, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    quant = 0

    for i in range(len(lis)):
        if lis[i] < 0:
            quant += 1 

    posi = []

    for i in range(len(lis)):
        if lis[i] < 0: 
            posi.append(i)
        

    soma = sum(posi)

    neg = []

    for i in range(len(lis)):
        if lis[i] < 0:
            neg.append(i)

    menorn = min(neg)
    maiorp = max(posi)

    dif = menorn - maiorp

    return quant, soma, menorn, maiorp, dif

def main():

    lis = [randint(-50, 50)for _ in range(20)]
    print(lis)

    quant, soma, menorn, maiorp, dif = calculos(lis)

    print(f'O maior par valor da lista é: {maiorp}')
    print(f'O menor impar valor da lista é: {menorn}')
    print(f'A soma dos valores positivos: {soma}')
    print(f'A diferencia do maior positivo e menor neagativo: {dif}')
    print(f'A quantidade de valores negativos: {quant}')
main()

#3. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O segundo maior valor da lista.
2. A quantidade de valores múltiplos de 3.
3. A média aritmética dos valores negativos.
4. A diferença entre o maior valor par e o menor valor ímpar (maior_par - menor_impar).
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -20 e 20, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    lis = sorted(lis)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            quant += 1 

    vn = []

    for i in range(len(lis)):
        if lis[i] < 0:
            vn.append(i)

    media = len(vn) / sum(vn)

    par = []
    imp = []

    for i in range(len(lis)):
        if lis[i] %2 == 0:
            par.append(i)
        else:
            imp.append(i)

    maiorp = max(par)
    menori = min(par)

    dif = maiorp - menori
     
    return lis[-2], quant, media, dif

def main():

    lis = [randint(-20, 20)for _ in range(15)]
    print(lis)

    lis[-2], quant, media, dif = calculos(lis)

    print(f'O segundo maior valor da lista é: {lis[-2]}')
    print(f'A quantidade de multiplos de 3: {quant}')
    print(f'A media dos valores negativos: {media}')
    print(f'A diferencia do maior positivo e menor neagativo: {dif}')
main()

#4. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O maior e o menor valor da lista.
2. A quantidade de valores divisíveis por 2 e por 3 ao mesmo tempo.
3. A soma dos valores ímpares.
4. A diferença entre o maior valor positivo e o menor valor negativo (maior_positivo - menor_negativo).
#O programa principal deve gerar e mostrar uma lista com 20 valores inteiros aleatórios entre -40 e 40, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0 

    for i in range(len(lis)):
        if lis[i] %2 == 0 and lis[i] %3 == 0:
            quant += 1 

    imp = []

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            imp.append(i)

    soma = sum(imp)

    positivo = []
    negativo = []

    for i in range(len(lis)):
        if lis[i] > 0:
            positivo.append(i)
        else:
            negativo.append(i)

    maiorp = max(positivo)
    menorn = min(negativo)

    dif = maiorp - menorn

    return maior, menor, quant, soma, dif

def main():

    lis = [randint(-40, 40)for _ in range(20)]
    print(lis)

    maior, menor, quant, soma, dif = calculos(lis)

    print(f'O maior numero da lista é: {maior}')
    print(f'O menor numero da lista é: {menor}')
    print(f'A quantidade de valores divisiveis por 3 e 2 ao mesmo tempo: {quant}')
    print(f'A soma dos valores impares: {soma}')
    print(f'A diferença entre o maior par e menor impar: {dif}')
main()

#5. Criar um programa com uma função que recebe uma lista com valores inteiros como parâmetro, calcula e retorna:
1. O maior e o menor valor par da lista.
2. A quantidade de valores múltiplos de 10.
3. A lista contendo os índices dos elementos negativos.
4. A média aritmética dos valores ímpares.
#O programa principal deve gerar e mostrar uma lista com 15 valores inteiros aleatórios entre -20 e 20, chamar a função passando a lista como parâmetro e mostrar os resultados retornados no final.

from random import randint 

def calculos(lis):

    maior = max(lis)
    menor = min(lis)

    quant = 0

    for i in range(len(lis)):
        if lis[i] %10 == 0:
            quant += 1 

    indice = []

    for i in range(len(lis)):
        if lis[i] < 0 :
            indice.append(i)

    imps = []

    for i in range(len(lis)):
        if lis[i] %3 == 0:
            imps.append(i)

    media = len(imps) / sum(imps)

    return maior, menor, quant, indice, media

def main():

    lis = [randint(-20, 20)for _ in range(15)]
    print(lis)

    maior, menor, quant, indice, media = calculos(lis)

    print(f'O maior valor da lista é: {maior}')
    print(f'O menor valor da lita é: {menor}')
    print(f'A quantidade de valores multiplos de 10: {quant}')
    print(f'Os indices dos valores negativos são: {indice}')
    print(f'A media dos valores negativos são: {media}')
main()
