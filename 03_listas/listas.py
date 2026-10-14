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
