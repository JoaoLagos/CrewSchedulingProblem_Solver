# Crew Scheduling Problem (CSP)

## Introdução
O **Problema de Escalonamento de Tripulação** (Crew Scheduling Problem - CSP) é um problema clássico de otimização em que o objetivo é designar tripulações para uma série de tarefas (como voos ou turnos) enquanto se minimizam custos operacionais ou se atendem restrições de tempo e regulações de trabalho.

**Exemplos de aplicação:**
- Escalonamento de pilotos e comissários em companhias aéreas.
- Designação de maquinistas para operações ferroviárias.
- Gerenciamento de turnos em empresas de transporte urbano.

## Objetivo do Projeto
Implementar algoritmos para resolver o problema de escalonamento de tripulação, garantindo a alocação eficiente de recursos humanos para tarefas específicas, respeitando restrições de trabalho e maximizando ou minimizando alguma função de interesse.

Para a entrega do trabalho (e apresentação) serão necessários cobrir os seguintes tópicos:
- O problema
- 2 meta-heurísticas
- A calibração de parâmetros efetuada (melhores parâmetros encontrados para os métodos)
- Valor médio da solução para 10 execuções
- Melhor solução encontrada em 10 execuções
- Tempo médio computacional para 10 execuções.

---

## POSSÍVEL Ideia Escolhida
> Possível pois não temos certeza ainda. A ideia (problema) escolhida, até o momento, foi retirada de: [https://people.brunel.ac.uk/~mastjjb/jeb/orlib/cspinfo.html](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/cspinfo.html)

### Programação da tripulação  
Atualmente, há 10 arquivos de dados.

Esses arquivos de dados são os dez problemas de teste do JEBeasley e B.Cao "Um algoritmo de busca em árvore para o agendamento de equipes problema" Revista Europeia de Pesquisa Operacional 94 (1996) págs. 517-526.

Os problemas de teste resolvidos naquele artigo estão disponíveis em os arquivos **csp50**, **csp100**, **csp150**, **csp200**, **csp250**, **csp300**, **csp350**, **csp400**, **csp450** e **csp500** (onde o número para cada arquivo csp é o número de tarefas).


**O formato desses arquivos de dados é:**
```
- número de tarefas (N), limite de tempo
- Para cada tarefa i (i=1,...,N): hora de início, hora de término
- Para cada arco de transição entre duas tarefas (i e j): i, j, custo de transição de i para j
```

O valor da solução ótima para cada um desses arquivos de dados para um número variável de tripulações é fornecido no artigo acima.

O maior arquivo é o csp500 de tamanho 250Kb (aproximadamente).  
O conjunto completo de arquivos tem tamanho de 900 KB (aproximadamente).

<!--
Até o momento, o cenário escolhido para este projeto é o de **Escalonamento de Tripulação para Companhias Aéreas**.

### Cenário

Uma companhia aérea precisa definir as escalas de tripulação para um conjunto de voos. Cada voo possui uma duração e horários específicos de partida e chegada. Cada tripulação tem um limite máximo de horas de trabalho permitidas por dia e por semana, e cada membro da tripulação tem um custo associado.

### O Problema
Como atribuir tripulações a voos de forma que todos os voos sejam cobertos, minimizando o custo total de tripulação e respeitando as restrições de jornada de trabalho.

### Elementos do CSP no Cenário
- **Tarefas**: Cada voo representa uma tarefa que precisa de tripulação.
- **Agentes**: Pilotos e comissários são os agentes que executam as tarefas.
- **Matriz de custos**: O custo de atribuir um voo a uma tripulação é definido pelo custo horário da tripulação.
- **Restrições**:
  - Limitação de horas de trabalho diárias e semanais.
  - Nenhum membro da tripulação pode estar designado a dois voos simultâneos.
- **Função Objetivo**: Minimizar o custo total de alocação de tripulações.

## Estrutura do Projeto
- **Solver**: Algoritmos de solução para escalonamento de tripulações.
- **Entrada**: Dados de voos, durações e custos de tripulações.
- **Saída**: Escalonamento otimizado para as tripulações, minimizando custos.
-->
