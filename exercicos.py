# Leia dois números inteiros digitados pelo usuário e exiba a soma, subtração, multiplicação e divisão entre eles.

def main():
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('\nDigite o segundo número: '))
    s = numero1 + numero2
    su = numero1 - numero2
    m = numero1 * numero2
    d = numero1 // numero2
    print(f'Soma: {s} Subtração: {su} Multiplicação: {m} Divisão: {d} ')
main ()

#Um vendedor recebe um salário fixo de R$ 1.200,00 mais uma comissão de 8% sobre o total de vendas do mês. Leia o valor total de vendas e calcule o salário final do vendedor.

def main():
    v = float(input('Digite o total de vendas do vendedor '))
    sf = 1.200
    c = 0.08
    tv = v * c
    s = sf + tv
    print(f'\nO salario final do vendedor é: {s}')
main()

#Leia a idade de uma pessoa e informe se ela é criança (até 12 anos), adolescente (13 a 17), adulto (18 a 59) ou idoso (60 ou mais).

def main():
    id = int(input(' Informe a idade: '))

    if id <= 12:
        print('\nA idade é de uma criança! ')
    elif id >= 13 and id <= 17:
        print('\nA idade é de um adolecente! ')
    elif id >= 18 and id <= 59:
        print('\nA idade é de um adulto! ')
    else:
        print('\nA idade é de um idoso! ')
main()

#Leia três notas de um aluno, calcule a média e informe se ele foi aprovado (média ≥ 7,0), ficou em recuperação (média entre 5,0 e 6,9) ou foi reprovado (média < 5,0).

def main():
    n1 = float(input('Digite a nota: '))
    n2 = float(input('Digite a nota: '))
    n3 = float(input('Digite a nota: '))
    m = 5.0
    mf = (n1 + n2 + n3) / 3
    print(f'a media final foi de: {mf:.2f}')

    if mf >= 7:
        print('APROVADO')
    elif mf < m :
        print('REPROVADO')
    else:
        print('RECUPERAÇÃO')
main()

#Leia um número e informe se ele é positivo, negativo ou zero. Se for positivo, informe também se é par ou ímpar.

def main():
    n = int(input('Digite um número :'))

    if n %2 == 0:
        print(' O numero é par!')
    else:
        print(' O numero é impar!')
main()

#Uma loja aplica desconto de acordo com o valor da compra: compras acima de R$ 500 têm 15% de desconto; entre R$ 200 e R$ 500 têm 10%; abaixo de R$ 200 não têm desconto.
# Leia o valor e exiba o desconto e o valor final.

def main():
    vc = float(input(' Digite o valor da compra: '))

    if vc >= 500.00:
        print(' Você teve 15% de desconto ')
    elif vc >= 200.00 and vc < 500.00:
        print(' Você teve 10% de desconto ')
    else:
        print(' Você não teve desconto!')
main()

#Leia o valor de um produto, a quantidade comprada e o percentual de desconto. Calcule e exiba o valor total sem desconto, o valor do desconto e o valor final a pagar.

def main():
    vp = float(input(' Digite o valor do produto: '))
    vd = float(input(' Valor do desconto obtido: '))
    d = vp - vd

    print(f'O valor sem desconto é de: {vp:.2f}')
    print(f'O valor com desconto é de: {d:.2f}')
main()

#Leia o nome de um aluno, sua altura em metros e seu peso em quilogramas. Calcule e exiba o IMC com duas casas decimais.

def main():
    n = input(' Digite seu nome: ')
    a = float(input('\nDigite sua altura(m): '))
    p = float(input('\nDigite seu peso(kg): '))
    imc = a ** 2 / p
    print(f'\nO IMC dessa pessoa é de {imc:.2}')
main()

#Leia o IMC de uma pessoa e classifique de acordo com a tabela da OMS: abaixo de 18.5 (abaixo do peso), 18.5 a 24.9 (peso normal), 25.0 a 29.9 (sobrepeso), 30.0 ou mais (obesidade).

def main():
    n = input(' Digite seu nome: ')
    a = float(input('\nDigite sua altura(m): '))
    p = float(input('\nDigite seu peso(kg): '))
    imc = a ** 2 / p
    print(f'\nO IMC dessa pessoa é de {imc:.2}')

    if p < 18.5:
        print('ABAIXO DO PESO!')
    elif p >= 18.5 and p < 24.9:
        print('PESO NORMAL!')
    elif p >= 25.0 and p < 29.9 :
        print('SOBREPESO!')
    else:
        print('OBESIDADE!')

main()

#Um estacionamento cobra R$ 5,00 pela primeira hora e R$ 3,00 por cada hora adicional. Leia o número de horas que o carro ficou e calcule e exiba o valor a pagar.
 #Se o cliente tiver cartão fidelidade, aplique 10% de desconto no total.

def main():
    hr = int(input('Quantas horas o carro ficou no estacionamento: '))
    cf = input('Possui cartão fidelidade? (s/n): ')

    if hr <= 1:
        total = 5.0
    else:
        total = 5.0 + (hr - 1) * 3.0

    if cf == 's':
        desconto = total * 0.1
    total -= desconto

    print(f'O valor a pagar é: R$ {total:.2f}')

main()

# Programa para calcular a área de um retângulo

def main():
    l1 = float(input(' Digite o valor do lado (m): '))
    l2 = float(input('\nDigite o valor do lado (m): '))
    area = l1 * l2
    print(f'\nA area do triangulo é de : {area}')
main()

lanche = ['lanche','suco','pizza','pudim']
lanche.append('picolé')
lanche.insert(0,'hot dog')
lanche.pop(3)
print(lanche[4])

valores = []
valores.append(5)
valores.append(8)
valores.append(9)

for c, v in enumerate(valores):
    print(f'na posição {c}, encontrei o valores {v}')
print('Cheguei ao final da lista!')

valores = []
for cont in range(0, 5):
    valores.append(int(input('\ndigite um valor:')))
    valores.sort()
for c, v in enumerate(valores):
    print(f'\nna posição {c}, encontrei o valores {v}')
print('\nCheguei ao final da lista!')

a = [2,3,4,7]
b = a [:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

teste = []
teste.append('Lucas')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste [1] = 22
galera.append(teste[:])
print(galera)

galera = [['lucas', 23], ['Maria', 22], ['João', 15]]
for p in galera:
    print(p)

Crie um programa que:

Leia 10 números inteiros.
Armazene os números em uma lista.
Mostre:
a lista completa;
a soma de todos os valores;
a média dos números.

def main():
    lis = []
    for cont in range(10):
            lis.append(int(input('\n Digite um valor: ')))
            lis.sort()
    print(f' \nA lista completa e ordenada dos 10 valores digitados é: {lis}')

    soma = sum(lis)
    print(f'\nA soma dos valores da lista é : {soma}')

    media = soma / len(lis)
    print(f'\nA média dos valores que estão na lista é de {media}')

main()

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

Leia 8 números inteiros.
Armazene em uma lista.
Mostre:
a lista original;
a lista em ordem crescente;
a lista em ordem decrescente.

def main():

    lis = []

    for cont in range(8):
        lis.append(int(input('Digite um valor inteiro: ')))

    lis_cres = sorted(lis)

    lis_decre = sorted(lis, reverse=True)

    print(f'\n A lista em ordem crescente fica: {lis_cres}')
    print(f'\n A lista em ordem descrecente fica: {lis_decre}')
    print(f'\n A lista original é: {lis} ')

main()

Exercício 5 — Contagem de ocorrências

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

Leia 12 números inteiros.
Depois peça outro número ao usuário.
Verifique:
se o número existe na lista;
em quais posições ele aparece.

def main():
    lis = []
    for i in range(1,13):
        lis.append(int(input(f'\n Digite o {i} numero: ')))

    pnum = int(input('\nDigite o numero que deseja achar na lista: '))

    posição = []

    for i in range(len(lis)):
        if lis[i] == pnum:
            posição.append(i)

    if len(posição) > 0:
        print(f'\n O numero {pnum}, existe na lista ')
        print(f'\nPosições encontradas {posição}')
    else:
        print('\nO numero não existe na lista ')
main()

Exercício 7 — Multiplicação dos elementos

Crie um programa que:

Leia 10 números inteiros.
Crie uma nova lista contendo o dobro de cada número.
Mostre:
lista original;
nova lista.

def main():
    lis = []

    for i in range(1, 11):
        lis.append(int(input(f'\n Digite o {i} numero:')))
    print(lis)

    lis2 = []

    for i in lis:
        mult = i ** 2
        lis2.append(mult)
    print(lis2)
main()

Exercício 8 — Remover valores repetidos

Crie um programa que:

Gere uma lista com 20 números aleatórios entre 1 e 15.
Crie uma nova lista sem valores repetidos.
Mostre:
lista original;
lista sem repetição.

from random import randint

def main():

    lis = ([randint(1, 15)for i in range(20)])

    #RETIRA A REPETIÇÃO DA LISTA CRIADA
    sem_rep = list(set(lis))

    print(f'\n Lista com repetição: {lis}')
    print(f'\n Lista sem repetição: {sem_rep}')
main()

Exercício 9 — Intercalar listas

Crie um programa que:

Leia 5 números para a lista A.
Leia 5 números para a lista B.
Crie uma lista C intercalando os elementos.

def main():
    lisA = []

    for i in range(1, 6):

        lisA.append(int(input(f'\n Digite o {i} valor: ')))

    lisB = []

    for i in range(1, 6):
        lisB.append(int(input(f'\n Digite o {i} valor da segunda lista: ')))

    lisC = []

    for i in range(5):
        lisC.append(lisA[i])
        lisC.append(lisB[i])

    print(f'\n A primeira lista é: {lisA}')
    print(f'\n A segunda lista é: {lisB}')
    print(f'\n As duas listas intercaladas ficaria: {lisC} ')
main()

Exercício 11 — Inverter lista

Crie um programa que:

Leia 10 números.
Mostre:
a lista original;
a lista invertida.

def main():

    lis = []
    for i in range(1, 11):
        lis.append(int(input(f'\nDigite o {i} valor: ')))
    print(f'\nLista: {lis}')

    lisi = sorted(lis, reverse = True)
    print(f'\nA lista invertida: {lisi}')
main()


Exercício 15 — Frequência dos números

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

Crie um programa que:

Leia as notas de 10 alunos.
Armazene em uma lista.
Mostre:
maior nota;
menor nota;
média da turma;
quantidade de aprovados (nota >= 6);
quantidade de reprovados;
lista das notas em ordem crescente.

def main():
    lis = []
    for i in range(1, 11):
        lis.append(float(input(f'Digite a nota do {i} aluno: ')))
    print(f'\n A lista de notas dos 10 alunos é: {lis}')

    maior = []
    maior.append(max(lis))
    print(f'\n A maior nota entre os alunos foi: {maior} ')

    menor = []
    menor.append(min(lis))
    print(f'\n A menor nota entre os alunos foi: {menor}')

    media = []
    media.append(sum(lis) / len(lis))
    print(f'\n A media entre os alunos foi: {media}')

    aprov = []
    for nota in (lis):
        if nota >= 6:
            aprov.append(nota)
    print(f'\n As notas aprovadas foram: {aprov}')

    reprov = []
    for nota in (lis):
        if nota < 6:
            reprov.append(nota)
    print(f'\nAs notas reprovadas são: {reprov}')

    list.sort(lis)
    print(f'\nA lista de notas crescente: {list}')
main()



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

Ler 4 valores inteiros e mostrar o maior valor negativo (menor que zero) entre eles. Caso não haja valores negativos, mostrar a mensagem "Não há valores negativos!".

def main():
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segundo valor:'))
    v3 = int(input('Digite o terceiro valor:'))
    v4 = int(input('Digite o quarto valor:'))

    if v1 < 0:
        print(f'O menor valor é {v1}')
    if v2 < v1:
        print(f'O menor valor é {v2}')
    if v3 < v2 :
        print(f'O menor valor é {v3}')
    if v4 < v3:
        print(f'O menor valor é {v4}')
    else:
        print('Não há valores negativos')
main()

Ler 5 valores inteiros e contar, sem usar lista ou estrutura de dados similar, quantos são pares e quantos são ímpares, mostrando os dois totais ao final.

def main():
    vals = []
    for i in range(1, 6):
        vals.append(int(input(f'Digite o {i} valor: ')))

    pares = 0
    impares = 0

    for i in range(len(vals)):
        if vals[i] % 2 == 0:
            pares += 1
    else:
        impares += 1

    print(f'A quantidade de valores pares que foi digitada foi de {pares}')
    print(f'A quantidade de valores impares que foi digitada foi de {impares}')
main()

Ler um valor inteiro representando a idade de uma pessoa e classificá-la como "Criança" (0 a 12 anos), "Adolescente" (13 a 17 anos), "Adulto" (18 a 59 anos) ou "Idoso" (60 anos ou mais). Caso o valor lido seja negativo, mostrar a mensagem "Idade inválida!".

def main():
    id = (int(input(' Digite a sua idade: ')))

    if id <= 12 :
        print('Criança')
    if id <= 17:
        print('Adolecente')
    if id <= 59:
        print('Adulto')
    if id >= 60:
        print('Idoso')
main()

Ler 4 valores inteiros e verificar, sem usar lista, se eles estão em ordem crescente. Mostrar "Estão em ordem crescente!" ou "Não estão em ordem crescente!".

def main():
    v1 = int(input('Digite o primeiro valor:'))
    v2 = int(input('Digite o segundo valor:'))
    v3 = int(input('Digite o terceiro valor:'))
    v4 = int(input('Digite o quarto valor:'))

    if v1 <= v2 and v2 > v1 and v3 > v2 and v4 > v3 :
        print('Estão em ordem crescente ')
    else:
        print('Não estão em ordem crescente ')
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

Crie um programa que leia 5 valores inteiros e, após as leituras, calcule e mostre o maior valor negativo (menor que zero) entre os 5 valores. Caso não haja nenhum valor negativo, mostre a mensagem: "Não há valores negativos!"

def main():
    v1 = int(input(' digite o 1 valor: '))
    v2 = int(input(' digite o 2 valor: '))
    v3 = int(input(' digite o 3 valor: '))
    v4 = int(input(' digite o 4 valor: '))
    v5 = int(input(' digite o 5 valor: '))

    cont = 0

    if v1 > 0:
        cont == v1
    if v2 < 0:
         if cont == 0 or v2 < 0:
            cont == v2
    if v3 < 0:
        if cont == 0 or v3 < 0:
            cont == v3
    if v4 < 0:
        if cont == 0 or v4 < 0:
            cont == v4
    if v5 < 0:
        if cont == 0 or v5 < 0:
            cont == v4
    else:
        print(' não há valores negativos.')


    print(f'{cont}')
main()

Crie um programa que leia 3 valores reais e, após as leituras, calcule e mostre o segundo maior valor entre os 3. O programa deve funcionar corretamente mesmo com valores repetidos.

def main():

    v1 = float(input("Digite o primeiro valor: "))
    v2 = float(input("Digite o segundo valor: "))
    v3 = float(input("Digite o terceiro valor: "))

    if (v1 >= v2 and v1 <= v3) or (v1 >= v3 and v1 <= v2):
        segundo_maior = v1
    elif (v2 >= v1 and v2 <= v3) or (v2 >= v3 and v2 <= v1):
        segundo_maior = v2
    else:
        segundo_maior = v3

    print("Segundo maior valor:", segundo_maior)
main()

Crie um programa que leia 6 valores inteiros e mostre quantos deles são pares e positivos ao mesmo tempo. Ao final, mostre também o maior entre os valores pares positivos encontrados. Se nenhum valor atender à condição, exiba: "Nenhum valor par e positivo encontrado."

def main():
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    v3 = int(input("Digite o terceiro valor: "))
    v4 = int(input("Digite o quarto valor: "))
    v5 = int(input("Digite o quinto valor: "))
    v6 = int(input("Digite o sexto valor: "))

    cont = 0

    if v1 > 0 and v1 %2 == 0:
        cont += 1
    if v2 > 0 and v2 %2 == 0:
        cont += 1
    if v3 > 0 and v3 %2 == 0:
        cont += 1
    if v4 > 0 and v4 %2 == 0:
        cont += 1
    if v5 > 0 and v5 %2 == 0:
        cont += 1
    if v6 > 0 and v6 %2 == 0:
        cont += 1
    else:
        print('Nenhum valor par e positivo')

    print(cont)
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

Crie um programa que leia 4 valores inteiros e, após as leituras, calcule e mostre a média somente dos valores positivos (maiores que zero). Caso não haja nenhum valor positivo, exiba: "Nenhum valor positivo para calcular a média!"

def main():
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    v3 = int(input("Digite o terceiro valor: "))
    v4 = int(input("Digite o quarto valor: "))

    media = (v1 + v2 + v3 + v4) / 4

    if v1 > 0 and v2 > 0 and v3 > 0 and v4 > 0:
        print(f'A media dos valores é de {media}')
    else:
        print('Nenhum valor positivo para calcular a média')
main()

Crie um programa que leia 5 valores inteiros e, após as leituras, mostre quantos deles são múltiplos de 2 ou de 3 (ou de ambos). Além disso, mostre o menor entre esses valores. Se nenhum valor satisfizer a condição, exiba: "Nenhum múltiplo de 2 ou 3 encontrado!"

def main():
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    v3 = int(input("Digite o terceiro valor: "))
    v4 = int(input("Digite o quarto valor: "))
    v5 = int(input("Digite o quinto valor: "))

    quant = 0

    if v1 %2 == 0 and v1 %3 == 0:
        quant += 1
    if v2 %2 == 0 and v3 %3 == 0:
        quant += 1
    if v4 %2 == 0 and v4 %3 == 0:
        quant += 1
    if v5 %2 == 0 and v5 %3 == 0:
        quant += 1
    else:
        print(' Nenhum multiplo de 2 ou 3 ')

    print(f'A quantidade de numeros multiplos de 2 ou 3 são: {quant}')
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

Crie um programa em Python para ler 5 valores inteiros e, após as leituras, calcular e mostrar o menor valor positivo (maior que zero) entre os valores informados.

Caso nenhum valor positivo seja digitado, exibir a mensagem:

“Nenhum valor positivo foi informado.”

OBS: NÃO é permitido utilizar listas, funções prontas como max(), min(), sum() ou operadores semelhantes do Python.

def main():
    v1 = int(input('Digite o 1 valor: '))
    v2 = int(input('Digite o 2 valor: '))
    v3 = int(input('Digite o 3 valor: '))
    v4 = int(input('Digite o 4 valor: '))
    v5 = int(input('Digite o 5 valor: '))



    if v1 > 0 or v1 < 0:

        print(f' O menor valor positivo é o {v1}')
    if v2 > 0 or  v2 < 0:

        print(f' O menor valor positivo é o {v2}')
    if v3 > 0 or  v3 < 0:

        print(f' O menor valor positivo é o {v3}')
    if v4 > 0 or  v4 < 0:

        print(f' O menor valor positivo é o {v4}')
    if v5 > 0 or  v5 < 0:

        print(f' O menor valor positivo é o {v5}')
    else:
        print('Nenhum valor positivo foi informado!')
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