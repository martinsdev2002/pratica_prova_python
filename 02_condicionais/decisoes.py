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
