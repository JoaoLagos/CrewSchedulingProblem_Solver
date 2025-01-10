# Estrutura dos Arquivos de Dados - Problema de Agendamento com Datas de Vencimento Comuns

Os arquivos de dados para o problema de agendamento com datas de vencimento comuns seguem a seguinte estrutura mostrada abaixo:

### Formato dos Dados

O formato dos arquivos de dados é:

```
- número de problemas
- Para cada problema por vez:
  - número de trabalhos (n)
  - Para cada trabalho i (i=1,...,n) por sua vez:
    - p(i), a(i), b(i)
```

Onde:
- **p(i)**: tempo de processamento do trabalho i
- **a(i)**: penalidade de antecipação para o trabalho i
- **b(i)**: penalidade de atraso para o trabalho i

A data de vencimento comum (**d**) é calculada por:

```
d = round[SOMA_P * h]
```

Onde:
- **SOMA_P**: soma dos tempos de processamento dos n trabalhos
- **h**: parâmetro usado para determinar a restrição da data de vencimento, variando entre 0,2; 0,4; 0,6; e 0,8
- **round[X]**: arredonda para o maior inteiro menor ou igual a X

### Exemplo Visual dentro do .txt

```
  10                    #Quantidade de Problemas
     10                 #Quantidade de Trabalhos (n) para o primeiro problema
     20     4     5     #p(i): tempo processamento, a(i):pen. antecip. e b(i): pen. atraso
     ..    ..   ..
     13    10     1
     ..
     ..
     ..
     10                 #Quantidade de Trabalhos (n) para o último problema
     16     2     6
     ..    ..   ..
     11     1    12
```

Os arquivos seguem essa estrutura para todos os conjuntos de dados: `sch10`, `sch20`, `sch50`, `sch100`, `sch200`, `sch500`, e `sch1000`.
