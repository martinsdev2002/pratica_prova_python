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

# Programa para calcular a área de um retângulo

def main():
    l1 = float(input(' Digite o valor do lado (m): '))
    l2 = float(input('\nDigite o valor do lado (m): '))
    area = l1 * l2
    print(f'\nA area do triangulo é de : {area}')
main()
