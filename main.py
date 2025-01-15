from problema_csp.crew_schedule import CrewSchedule
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

agendamento = CommonDueDateSchedule("problema_sch/arquivos_sch/sch10.txt", 0.6)

agendamento.exibir_informacoes()

print(agendamento.calcular_penalidades_para_problema(0))