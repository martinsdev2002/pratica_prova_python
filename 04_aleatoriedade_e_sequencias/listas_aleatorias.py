Crie um programa que:

Gere uma lista com 15 números aleatórios entre 1 e 100.
Mostre:
a lista;
o maior valor;
o menor valor;
as posições onde o maior número aparece.

from random  import randint

def main():

    # cria a lista aleatoria de 0 a 100 entre 15 numeros
    lista = ([randint(0, 100)for i in range(15)])
    print(f'A lista criada com numeros aleatorios é: {lista}')

    #verifica o numero maior e menor da lista e exibe
    menor = min(lista)
    maior = max(lista)
    print(f'\n O menor numero da lista é {menor} e o maior numero da lista é {maior} ')

    #mostra o maior numero e o indice que ele está localizado na lista
    lista_maior = lista.index(maior)
    print(f'\n O maior numero da lista é: {maior}, que está no indice {lista_maior}')

main()

Exercício 3 — Pares e ímpares

Crie um programa que:

Gere uma lista com 20 números aleatórios entre 1 e 50.
Separe os números em:
lista de pares;
lista de ímpares.
Mostre as três listas.

from random import randint

def main():
    # cria lista aleatoria com 20 numeros entre os numeros 1 e 50
    lis = ([randint(1, 50)for i in range(20)])

    pares = []
    impares = []

    #Varrendo a lista original e separando os elementos
    for numero in lis:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print(f'\n A lista original aleatoria é {lis}')
    print(f'\n A lista de pares é {pares}')
    print(f'\n A lista de impares é {impares}')

main()

Exercício 4 — Ordenação

Crie um programa que:

Gere uma lista com 20 números aleatórios entre 1 e 10.
Mostre:
a lista;
quantas vezes cada número aparece.

from random import randint

def main():

    #cria uma lista aleatoria de 1 a 10 entre 1 e 20
    lista = ([randint(1, 10)for i in range(20)])

    #percorre a lista e mostra quantas vezes o numero apareceu na lista
    for numeros in range(1, 10):
        qnt = lista.count(numeros)
        print(f'\nA quantidade de vezes que {numeros} apareceu foi de {qnt}')


    print(f'\nA lista aleatória é: {lista}')
main()

Exercício 6 — Buscar número na lista

Crie um programa que:

Gere uma lista com 30 números aleatórios entre 1 e 5.
Mostre qual número apareceu mais vezes na lista.

from random import randint

def main():

    lis = ([randint(1, 6) for _ in range(30)])

    print(f'\n Lista: {lis}')

    num = []
    for numero in range(1, 6):
        num.append(lis.count(numero))

    print(f'\nO numero que mais apareceu na lista: {num}')
main()

Exercício 16 — Sistema de análise de notas

### **`6.`** Execute as seguintes tarefas:
+ ### Criar e mostrar uma lista com 20 valores aleatórios entre 0 e 9. Pode ter valores repetidos.
+ ### Mostrar os 3 menores valores distintos contidos na lista.
+ ### Mostrar uma msg (Sim ou Não) se o número `1` aparece na lista antes de um `0` (seguidos). Apenas uma msg deve ser mostrada.
+ ### Calcular e mostrar qual ou quais valores mais aparecem na lista.

from random import randint

def main():
    lis = ([randint(0, 9)for _ in range(20)])
    print(lis)

    lis = sorted(set(lis))
    print(lis)
    print(lis [:3])
main()

Gerar e mostrar uma lista com 100 valores inteiros aleatórios entre 0 e 50 e calcular quantas vezes ocorre uma sequência de três valores iguais seguidos (o mesmo valor repetido três vezes consecutivas).

from random import randint
def main():

    lis = [randint(0, 50)for _ in range(100)]

    contador = 0

    for i in range(len(lis)-2):
        if lis[i] == lis[i + 1] == lis[i+2]:
            contador += 1

    print(lis)
    print(f' os valores se repetem {contador} vezes!')

main()

Crie um programa que gere e mostre uma lista com 50 valores inteiros aleatórios entre 1 e 20 e, em seguida, realize as seguintes tarefas:

Calcular e mostrar a quantidade de vezes que o valor 10 aparece na lista.
Calcular e mostrar a soma de todos os valores ímpares da lista.

from random import randint
def main():

    lista = [randint(1, 20)for _ in range(50)]
    print(lista)

    cont = 0

    for i in lista:
        if i == 10:
            cont += 1

    print(f'A quantidade que o valor 10 aparece na lista é {cont}')

    quant = 0

    for i in lista:
        if i %3 == 0:
            quant += 1

    print(f' A quantidade de numeros inpares da lista foi {quant}')
main()

Crie um programa que gere e mostre uma lista com 80 valores inteiros aleatórios entre 0 e 50 e, em seguida, realize as seguintes tarefas:

Calcular e mostrar quantas vezes um valor aparece imediatamente antes de um valor maior que ele (ou seja, pares consecutivos em ordem crescente).
Calcular e mostrar os dois menores valores múltiplos de 5 presentes na lista.

from random import randint
def main():

    lista = [randint(0, 50)for _ in range(80)]
    print(lista)

    quant = 0

    for i in range(len(lista)):
        if lista[i] >= lista[i-1]:
            quant += 1
    print(f'A quantidade que aparece é de {quant} ')

    cont = 0

    for i in range(len(lista)):
        if lista[i] %5 == 0:
            cont += 1
    print(f' A quantidade de valores multiplos de 5 é: {cont}')

main()

Crie um programa que gere e mostre uma lista com 60 valores inteiros aleatórios entre 10 e 40 e, em seguida, realize as seguintes tarefas:

Calcular e mostrar a quantidade de vezes que um valor é seguido de um valor igual a ele menos 1 (ou seja, pares consecutivos decrescentes com diferença de 1).
Calcular e mostrar o maior e o segundo maior valor múltiplo de 4 da lista. Se não houver ao menos dois múltiplos de 4, exiba uma mensagem adequada.

from random import randint
def main():
    lista = [randint(10, 40)for _ in range(60)]
    print(lista)

    quant = 0

    for i in range(len(lista)):
        if lista[i] == lista[i] and lista[i - 1]:
            quant += 1
    print(f' O valor é igual ou seguido por ele mesmo {quant} vezes! ')

    cont = 0

    for i in range(len(lista)-1):
        if lista[i] %4 == 0 or lista[i] == max(lista):
            cont += 1
        else:
            print('não há multiplos de 4')
        break

    print(f'{cont}')
main()

Crie um programa que gere e mostre uma lista com 70 valores inteiros aleatórios entre 0 e 25 e, em seguida, execute as tarefas:

Calcular e mostrar quantas vezes um valor aparece seguido de um valor menor que ele (pares consecutivos em ordem decrescente).
Calcular e mostrar os dois menores valores múltiplos de 7 da lista. Se não houver ao menos dois, exibir mensagem adequada.

from random import randint
def main():

    lista = [randint(0, 25)for _ in range(70)]
    print(lista)

    quant = 0
    for i in range(len(lista)):
        if lista[i] == lista[i] < lista[i]:
            quant += 1
    print(quant)

    cont = 0
    for i in range(len(lista)- 2):
        if lista[i] <= lista[i] %7 == 0:
            cont += 1
        else:
            print('não existem dois numeros menos multiplos de 7 ')
        break
    print(cont)
main()

Crie um programa que gere e mostre uma lista com 90 valores inteiros aleatórios entre 5 e 35 e, em seguida, execute as tarefas:

Calcular e mostrar quantas vezes um valor é igual ao dobro do valor anterior na lista.
Calcular e mostrar a soma de todos os valores múltiplos de 6 presentes na lista.

from random import randint
def main():

    lis = [randint(5, 35)for _ in range(90)]
    print(lis)

    quant = 0

    for i in range(len(lis)- 1):
        if lis[i] == lis[i + 1]:
            quant += 1

    print(quant)

    soma = 0

    for valores in range(len(lis)):
        if lis[valores] %6 == 0:
            valores += soma

    print(soma)
main()

Crie um programa que gere e mostre uma lista com 120 valores inteiros aleatórios entre 0 e 40 e, em seguida, execute as tarefas:

Calcular e mostrar quantas vezes três valores consecutivos são todos iguais (triplas iguais seguidas).
Calcular e mostrar o maior valor que seja simultaneamente múltiplo de 2 e de 5 da lista. Se não houver, exibir mensagem adequada.

from random import randint
def main():

    lis = [randint(0, 40)for _ in range(120)]
    print(lis)

    quant = 0

    for i in range(len(lis)- 2):
        if lis[i] == lis[i+1] and lis[i] == lis[i+2]:
            quant += 1
    print(quant)

    maior = 0

    for valor in lis:
        if valor %2 == 0 and valor %5 == 0:
            valor = maior
        if valor > maior:
                maior = valor

    if maior > 0:
        print(f'O maior valor múltiplo de 2 e 5 é {maior}')
    else:
        print('Não há valores múltiplos de 2 e 5 na lista.')
main()

Crie um programa em Python para gerar uma lista com 80 valores inteiros aleatórios entre 0 e 20 e, em seguida, executar as seguintes tarefas:

Mostrar a lista gerada.
Calcular e mostrar quantas vezes um número é seguido imediatamente pelo mesmo número (valores iguais consecutivos).
Calcular e mostrar o maior valor que aparece em posições consecutivas na lista.

from random import randint
def main():
    lis = [randint(0, 20)for i in range(80)]
    print(lis)

    cont = 0

    for i in range(len(lis) - 1):
        if lis[i] == lis[i + 1] and lis[i] >= lis[i + 1]:
            cont += 1
    print(cont)
main()

Crie um programa em Python para gerar uma lista com 100 valores inteiros aleatórios entre 1 e 50 e, em seguida:

Mostrar a lista gerada.
Encontrar e mostrar os dois maiores valores pares da lista.
Caso exista apenas um valor par, mostrar apenas ele.
Caso não exista nenhum valor par, exibir uma mensagem apropriada.

from random import randint
def main():
    lis = [randint(1, 50)for i in range(100)]
    print(lis)

    par = 0

    for i in lis:
     if i %2 == 0:
        par += 1

    if par > 0:
        print(f'A quantidade de maiores valores pares na lista é de: {par}')
    else:
        print('Não há valores pares na lista ')
main()

Crie um programa em Python para gerar uma lista com 120 valores inteiros aleatórios entre 0 e 60 e, em seguida:

Mostrar a lista gerada.
Calcular quantos valores da lista são múltiplos de 5.
Calcular a soma de todos os múltiplos de 5 encontrados.
Mostrar o maior múltiplo de 5 da lista.

from random import randint
def main():
    lis = [randint(0, 60)for i in range(120)]
    print(lis)

    m5 = 0

    for i in lis:
        if i %5 == 0:
            m5 += 1

    print(f'A quantidade de numeros multiplos de 5 são de {m5} ')

    lism = []

    for i in lis:
        if i %5 == 0:
            lism.append(i)

    soma = sum(lism)
    print(soma)
main()

Crie um programa em Python para gerar uma lista com 90 valores inteiros aleatórios entre 0 e 15 e, em seguida:

Mostrar a lista gerada.
Calcular quantas vezes aparecem três valores iguais consecutivos na lista.
Exemplo: 7, 7, 7 conta como uma ocorrência.
Mostrar a quantidade total encontrada.

from random import randint
def main():

    lis = [randint(0, 15)for i in range(90)]
    print(lis)

    cont = 0

    for i in range(len(lis)- 2):
        if lis[i] == lis[i + 1] and lis[i] == lis[i + 2]:
            cont += 1

    print(f'A quantidade total encontrada é de {cont}')
main()

from random import randint
def main():

    lis = [randint(0, 30) for i in range(100)]
    print(lis)

    cont = 0

    for i in range(len(lis)- 1):
        if lis[i] == lis[i+1]:
            cont += 1

    print(f'A quantidade de vezes que um numero fica seguido dele mesmo é {cont} ')

    mult = []

    for i in lis:
        if i %3 == 0:
            mult.append(i)

    print(mult)
main()

def main():
    v1 = int(input('digite o primeiro numero: '))
    v2 = int(input('digite o primeiro numero: '))
    v3 = int(input('digite o primeiro numero: '))

    cont = 0

    if v1 < v2 or v1 == v2:
        cont += 1
    if v2 < v1 or v2 == v1:
        cont += 1
    if v3 < v2 or v3 == v2:
        cont += 1

    print(cont)
main()


from random import randint
def main():
    lis = [randint(-50, 50)for _ in range(200)]
    print(lis)

    cont = 0

    for i in lis:
        if lis[i] %5 == 0 and lis[i] < 0 :
            cont += 1

    print(cont)

    lis2 = []

    co1 = lis[:15]
    lis2.append(co1)
    co2 = lis[15:]
    lis2.append(co2)

    media = sum(lis2) / len(lis2)

    print(media)
main()
