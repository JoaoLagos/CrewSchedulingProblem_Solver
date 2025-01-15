from busca_tabu import TabuSearch
from problema_sch.common_due_date_schedule import CommonDueDateSchedule


# Carregar o agendamento de tarefas a partir do arquivo
#agendamento = CrewSchedule("problema_csp/arquivos_csp/csp50.txt")

# Exibir as informações do agendamento
#agendamento.exibir_informacoes()

# Acessar tarefas diretamente usando o dicionário
#tarefas = agendamento.obter_tarefas()
#print(f"Primeira tarefa (Tarefa 1): {tarefas[1]}")  # Acessa a tarefa com chave 1

# Acessar transições diretamente
#transicoes = agendamento.obter_transicoes()
#print(f"Primeira transição: {transicoes[0]}")

# Inicializa o arquivo em questão
agendamento = CommonDueDateSchedule("problema_sch/arquivos_sch/sch10.txt", 0.6)

# Inicializa a meta-heurística BUSCA TABU
busca_tabu = TabuSearch(agendamento)
# Executa a BUSCA TABU
for problema in agendamento.problemas:
    print(f"EXECUÇÃO: {problema.nome}")
    busca_tabu.executar(problema)