import time
import pandas as pd
from busca_tabu import TabuSearch
from busca_simulated_annealing import SimulatedAnnealing
from problema_sch.common_due_date_schedule import CommonDueDateSchedule
import os

# Lista de valores de h para testar
h_values = [0.2, 0.4, 0.6, 0.8]

# Inicializa as listas para armazenar os resultados
resultados_tabu = []
resultados_sa = []

tempo_total_tabu = 0
tempo_total_sa = 0

# Cria a pasta 'resultados' se ela não existir
os.makedirs("resultados", exist_ok=True)

nome_arquivo = "sch20.txt"
# Executa as meta-heurísticas para cada valor de h
for h in h_values:
    print("----------------------------------------")
    print(f"Processando Meta-heurísticas para h={h}")
    print("----------------------------------------")
    # Inicializa o agendamento com o valor atual de h
    agendamento = CommonDueDateSchedule(f"problema_sch/arquivos_sch/{nome_arquivo}", h)

    # Inicializa as meta-heurísticas
    busca_tabu = TabuSearch(agendamento)
    simulated_annealing = SimulatedAnnealing(agendamento)

    # Inicia o contador de tempo
    start_time = time.time()
    # Executa para cada problema no agendamento
    for k, problema in enumerate(agendamento.problemas, start=1):
        # Executa a BUSCA TABU
        custo_tabu, melhor_solucao_tabu = busca_tabu.executar(problema)
        resultados_tabu.append((k, h, custo_tabu))
        print("Processando Busca Tabu...")
    # Calcula o tempo de execução do TABU
    end_time = time.time()
    tempo_tabu = end_time - start_time  # Tempo em segundos
    tempo_total_tabu += tempo_tabu

    # Inicia o contador de tempo
    start_time = time.time()
    for k, problema in enumerate(agendamento.problemas, start=1):
        # Executa o SIMULATED ANNEALING
        custo_sa, melhor_solucao_sa = simulated_annealing.executar(problema)
        resultados_sa.append((k, h, custo_sa))
        print("Processando Simulated Annealing...")
    # Calcula o tempo de execução do TABU
    end_time = time.time()
    tempo_sa = end_time - start_time  # Tempo em segundos
    tempo_total_sa += tempo_sa

# Cria DataFrames para os resultados
df_tabu = pd.DataFrame(resultados_tabu, columns=['k', 'h', 'Custo'])
df_sa = pd.DataFrame(resultados_sa, columns=['k', 'h', 'Custo'])

# Pivot para formatar a tabela
tabela_tabu = df_tabu.pivot(index='k', columns='h', values='Custo')
tabela_sa = df_sa.pivot(index='k', columns='h', values='Custo')

# Exibe as tabelas no console
print('\n')
print(f"Resultados Tabu Search: (Tempo: {tempo_total_tabu:.4f} segundos)")
print(tabela_tabu)

print(f"\nResultados Simulated Annealing: (Tempo: {tempo_total_sa:.4f} segundos)")
print(tabela_sa)

# Salva os resultados em arquivos .txt na pasta 'resultados'
with open(f'resultados/resultado_{nome_arquivo}', 'w') as f:
    f.write("===================================\n")
    f.write(f"RESULTADO PARA {nome_arquivo}\n")
    f.write("===================================\n\n")
    f.write("============================TABU SEARCH============================\n")
    f.write(f"Resultados Tabu Search:   (Tempo: {tempo_total_tabu:.4f} segundos)\n")
    f.write(tabela_tabu.to_string())
    f.write("\n--------------------------------------")
    f.write("\nMelhor Solucao do Busca Tabu:\n")
    for i, trabalho in enumerate(melhor_solucao_tabu, start=1):
        f.write(f"   {i:>2}. {trabalho.nome}\n")
    f.write("====================================================================")
    


    f.write("\n\n\n==========================SIMULATED ANNEALING===========================\n")
    f.write(f"Resultados Simulated Annealing:   (Tempo: {tempo_total_sa:.4f} segundos)\n")
    f.write(tabela_sa.to_string())
    f.write("\n-------------------------------------------------")
    f.write("\nMelhor Solucao do Simulated Annealing:\n")
    for i, trabalho in enumerate(melhor_solucao_sa, start=1):
        f.write(f"   {i:>2}. {trabalho.nome}\n")
    f.write("====================================================================")
