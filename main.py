import pandas as pd
from busca_tabu import TabuSearch
from busca_simulated_annealing import SimulatedAnnealing
from problema_sch.common_due_date_schedule import CommonDueDateSchedule

# Lista de valores de h para testar
h_values = [0.2, 0.4, 0.6, 0.8]

# Inicializa as listas para armazenar os resultados
resultados_tabu = []
resultados_sa = []

# Executa as meta-heurísticas para cada valor de h
for h in h_values:
    # Inicializa o agendamento com o valor atual de h
    agendamento = CommonDueDateSchedule("problema_sch/arquivos_sch/sch10.txt", h)

    # Inicializa as meta-heurísticas
    busca_tabu = TabuSearch(agendamento)
    simulated_annealing = SimulatedAnnealing(agendamento)

    # Executa para cada problema no agendamento
    for k, problema in enumerate(agendamento.problemas, start=1):
        # Executa a BUSCA TABU
        custo_tabu, _ = busca_tabu.executar(problema)
        resultados_tabu.append((k, h, custo_tabu))

        # Executa o SIMULATED ANNEALING
        custo_sa, _ = simulated_annealing.executar(problema)
        resultados_sa.append((k, h, custo_sa))

# Cria DataFrames para os resultados
df_tabu = pd.DataFrame(resultados_tabu, columns=['k', 'h', 'Custo'])
df_sa = pd.DataFrame(resultados_sa, columns=['k', 'h', 'Custo'])

# Pivot para formatar a tabela
tabela_tabu = df_tabu.pivot(index='k', columns='h', values='Custo')
tabela_sa = df_sa.pivot(index='k', columns='h', values='Custo')

print('\n')
# Exibe as tabelas
print("Resultados Tabu Search:")
print(tabela_tabu)

print("\nResultados Simulated Annealing:")
print(tabela_sa)