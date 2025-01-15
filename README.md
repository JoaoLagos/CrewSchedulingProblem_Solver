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

## Ideia Escolhida

> A ideia (problema) escolhida, até o momento, foi retirada de: [https://people.brunel.ac.uk/~mastjjb/jeb/orlib/schinfo.html](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/schinfo.html)

### Agendamento de Datas de Vencimento Comuns
Atualmente, há 7 arquivos de dados.

Esses arquivos de dados correspondem aos benchmarks usados no problema de datas de vencimento comuns restritas para uma única máquina, como descrito por JEBeasley e outros em vários estudos de pesquisa operacional.

Os problemas de teste resolvidos abrangem os arquivos **sch10**, **sch20**, **sch50**, **sch100**, **sch200**, **sch500**, e **sch1000**, onde o número no nome do arquivo indica a quantidade de trabalhos envolvidos.

**O formato desses arquivos de dados é:**
```
- número de problemas
- Para cada problema por vez:
  - número de trabalhos (n)
  - Para cada trabalho i (i=1,...,n) por sua vez:
    - p(i), a(i), b(i)
```

Onde:
- `p(i)` é o tempo de processamento do trabalho i.
- `a(i)` é a penalidade aplicada se o trabalho i for concluído antes da data de vencimento comum d (adiantamento).
- `b(i)` é a penalidade aplicada se o trabalho i for concluído após a data de vencimento comum d (atraso).

A data de vencimento comum `d` é calculada como:

```
d = round[SOMA_P * h]
```

Onde:
- `SOMA_P` denota a soma dos tempos de processamento de todos os n trabalhos.
- `h` é um parâmetro que determina o grau de restrição da data de vencimento comum. Para os benchmarks fornecidos, os valores de `h` usados são 0,2; 0,4; 0,6; e 0,8.

O conjunto completo de benchmarks inclui 280 problemas, abrangendo diferentes combinações de número de trabalhos e parâmetros de restrição de datas de vencimento, e pode ser encontrado no site citado acima.


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
