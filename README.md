# Exercícios de Python

Este repositório reúne exercícios feitos à mão durante o estudo de Python. O material está concentrado principalmente em [`exercicos.py`](./exercicos.py), um arquivo de prática com enunciados, tentativas e soluções de problemas diferentes.

## O que há no arquivo

O arquivo percorre os fundamentos da programação por meio de pequenos programas de entrada, processamento e saída. Os exemplos abaixo são um mapa dos assuntos e dos tipos de problema presentes no material; não representam módulos separados nem indicam que todas as tentativas já foram revisadas.

### Entrada, saída e variáveis

- Leitura de dados digitados com `input()`.
- Conversão de texto para números inteiros e reais usando `int()` e `float()`.
- Armazenamento de valores e resultados em variáveis.
- Exibição de resultados com `print()` e mensagens formatadas com f-strings.
- Formatação de números decimais, por exemplo, para apresentar valores monetários ou médias.

### Operações e cálculos

Os exercícios iniciais praticam soma, subtração, multiplicação, divisão e divisão inteira. Também aparecem:

- Resto da divisão (`%`) para verificar paridade e múltiplos.
- Potência (`**`) em fórmulas matemáticas.
- Cálculos de médias, comissões, descontos e valores finais.
- Cálculo de área de retângulo e de índice de massa corporal (IMC).
- Comparações entre valores para identificar maior, menor, segundo maior e valores dentro de uma faixa.

### Decisões e regras de negócio

O uso de `if`, `elif` e `else`, junto com operadores de comparação e operadores lógicos `and` e `or`, é praticado em problemas como:

- Classificar idades em faixas.
- Determinar aprovação, recuperação ou reprovação a partir de notas.
- Identificar números positivos, negativos, zero, pares e ímpares.
- Aplicar faixas de desconto a compras e desconto de fidelidade em estacionamento.
- Conferir se valores estão em ordem crescente.
- Encontrar valores que atendem simultaneamente a mais de uma condição, como ser positivo e par.
- Tratar situações sem resultados válidos, como não haver valores positivos ou negativos.

### Repetição, contadores e acumuladores

- Laços `for` e `range()` para repetir leituras e processar quantidades definidas de dados.
- Percurso dos elementos de uma coleção, diretamente ou usando índices.
- Contadores incrementados para registrar quantas vezes uma condição ocorre.
- Acumuladores para somar valores selecionados.
- Análise de relações entre elementos consecutivos, incluindo pares em ordem crescente ou decrescente e sequências de valores iguais.

### Listas

Uma parte extensa das atividades trabalha com listas:

- Criar listas vazias e preenchê-las com `append()`.
- Acessar e atualizar itens por índice, e percorrer listas com `enumerate()`.
- Inserir e remover itens, por exemplo com `insert()` e `pop()`.
- Copiar uma lista com fatiamento (`[:]`) e observar a diferença entre cópia e referência.
- Criar listas de listas para agrupar dados.
- Ordenar valores em ordem crescente ou decrescente.
- Intercalar duas listas e produzir listas novas a partir de critérios.
- Usar operações e funções comuns como `count()`, `sum()`, `min()`, `max()`, `sorted()` e `set()`.

Os problemas incluem listas informadas pelo usuário e listas geradas aleatoriamente. Entre os resultados pedidos estão a lista completa, soma, média, maior e menor valor, posições de ocorrências, valores sem repetição, valores pares e ímpares e frequência dos itens.

### Números aleatórios e análise de sequências

O módulo `random`, por meio de `randint()`, é usado para criar listas de números de diferentes tamanhos e intervalos. Sobre esses dados, as atividades propõem:

- Separar valores pares e ímpares.
- Contar ocorrências de um número e localizar as posições em que aparece.
- Encontrar valores distintos, extremos e múltiplos de determinados números.
- Calcular somas, médias e frequências condicionais.
- Identificar repetições consecutivas, como dois ou três valores iguais seguidos.
- Comparar valores vizinhos e localizar padrões ou mudanças entre posições.
- Analisar notas de uma turma, como média, extremos e quantidade de aprovados e reprovados.

### Funções

Nas atividades posteriores, as soluções começam a separar tarefas em funções:

- Definir funções com `def`, receber parâmetros e chamá-las a partir de `main()`.
- Retornar resultados usando `return`.
- Devolver mais de um resultado e distribuí-los em variáveis no momento da chamada.
- Receber listas e valores de busca como parâmetros.
- Criar funções para contar ocorrências, pesquisar valores, retornar índices, filtrar itens e calcular estatísticas.

Há exemplos de buscas por primeira e última ocorrência, identificação de valores únicos, seleção de itens por intervalo ou por comparação com um valor de referência e cálculo de estatísticas como extremos, contagens, somas, médias e diferenças.

## Aprendizados praticados

Em conjunto, os exercícios ajudam a praticar como:

1. Interpretar um enunciado e identificar dados de entrada, processamento e resultado esperado.
2. Traduzir regras em condições e cálculos.
3. Repetir operações sem escrever cada uma manualmente.
4. Escolher entre trabalhar com valores individuais e armazenar dados em listas.
5. Percorrer dados, guardar resultados parciais e construir novas listas.
6. Dividir uma tarefa em funções menores e retornar resultados para o programa principal.
7. Considerar limites e casos sem resultado, como listas sem itens que satisfaçam uma condição.
8. Testar o comportamento com entradas diferentes e comparar a saída obtida com o enunciado.

## Como o material está organizado

`exercicos.py` é um caderno de estudos em forma de código, não um aplicativo único. Os exercícios são independentes e aparecem em sequência; há várias definições e chamadas de `main()`, além de enunciados e anotações entre as soluções. Parte dos enunciados está escrita como texto fora de comentários e algumas tentativas ainda precisam de correção. Por isso, executar o arquivo inteiro pode resultar em erro e não é garantia de que todas as atividades rodem corretamente.

Para estudar ou testar uma atividade, localize seu enunciado, leia o trecho correspondente e execute-o isoladamente. Compare o resultado com o que foi pedido e experimente diferentes entradas, inclusive valores de limite e casos em que nenhum item atende à condição. Os rascunhos fazem parte do processo de aprendizado e podem ser revisados à medida que os conceitos forem sendo praticados.
