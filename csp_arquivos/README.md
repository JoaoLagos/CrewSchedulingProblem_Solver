# Estrutura dos Arquivos de Dados - Problemas CSP

Os arquivos de dados para os problemas CSP seguem a seguinte estrutura mostrada abaixo:

### Formato dos Dados

O formato dos arquivos de dados é:
```
- número de tarefas (N), limite de tempo
- Para cada tarefa i (i=1,...,N): hora de início, hora de término
- Para cada arco de transição entre duas tarefas (i e j): i, j, custo de transição de i para j
```

### Exemplo Visual dentro do .txt
```
50 480     # 50: Número de Tarefas; 480: Limite de tempo (parece ser em minutos)
1 144      # 1: Minuto Início; 144: Minuto Final (Os abaixo tem o mesmo esquema)
.. ...
1 10 169   # 1: Tarefa 1; 10: Tarefa 10; 169: Custo para transicionar da tarefa 1 para a 10 (não sei em que unidade é isso, se é valor($), se é tempo, não faço ideia) (Os abaixo tem o mesmo esquema)
. .. ...
```

