import copy
import random
from algoritmo_construtivo import AlgoritmoConstrutivo
from problema_sch.common_due_date_schedule import CommonDueDateSchedule

def gerar_movimento(s):
    # Gera um movimento aleatório combinando swap, shift e move um trabalho de lugar
    trabalhos = copy.deepcopy(s)  # Supondo que s seja a lista de trabalhos
    
    # Troca (swap) entre dois trabalhos aleatórios
    i, j = random.sample(range(len(trabalhos)), 2)  # Seleciona dois índices aleatórios
    trabalhos[i], trabalhos[j] = trabalhos[j], trabalhos[i]  # Troca as posições
        
    
    
    return copy.deepcopy(trabalhos)

def avaliar_custo(movimento, data_vencimento_comum):
    tempo_acumulado = 0
    penalidade_total = 0

    for trabalho in movimento:
        tempo_acumulado += trabalho.tempo_processamento

        # Calculando as penalidades diretamente
        if tempo_acumulado < data_vencimento_comum:  # Antecipação
            penalidade = (data_vencimento_comum - tempo_acumulado) * trabalho.custo_antecipado
        elif tempo_acumulado > data_vencimento_comum:  # Atraso
            penalidade = (tempo_acumulado - data_vencimento_comum) * trabalho.custo_atraso
        else:  # Nenhuma penalidade, caso não haja antecipação nem atraso, ou seja, tempo de término do trabalho é EXATAMENTE IGUAL ao vencimento_comum
            penalidade = 0

        # Somando a penalidade total
        penalidade_total += penalidade

    return penalidade_total


# Inicializa o agendamento com o arquivo e o parâmetro h
agendamento = CommonDueDateSchedule("problema_sch/arquivos_sch/sch10.txt", 0.6)

# Inicia a solução construtiva para o primeiro problema
data_comum = agendamento.problemas[0].data_vencimento_comum
s = AlgoritmoConstrutivo(agendamento.problemas[0]).gerar_solucao_inicial()
s_ = copy.deepcopy(s)  # Solução inicial
iter = 0
melhor_iter = 0
lista_tabu = []

# Critério de parada: número máximo de iterações
max_iteracoes = 500
melhor_solucao = copy.deepcopy(s_)  # Solução inicial como melhor

#print(avaliar_custo(s_, data_comum))
while iter < max_iteracoes:
    iter += 1
    
    # Gera o movimento ou a solução vizinha
    movimento = gerar_movimento(melhor_solucao)

    # Verifica se o movimento está na lista tabu
    if movimento not in lista_tabu:
        custo_movimento = avaliar_custo(movimento, data_comum)
        custo_melhor = avaliar_custo(melhor_solucao, data_comum)
        #print(custo_movimento, custo_melhor)
        if custo_movimento < custo_melhor:
            melhor_solucao = copy.deepcopy(movimento)
            melhor_iter = iter
            lista_tabu.append(movimento)
            if len(lista_tabu) > 10:
                lista_tabu.pop(0)

    else:
        # Se o movimento está na lista tabu, simplesmente não faz nada
        pass

    # Se algum critério de sucesso for atingido, podemos parar
    # Aqui, você pode adicionar o critério de sucesso se desejar

    # Exemplo de impressão da melhor solução até o momento
    if iter % 1 == 0:  # Exibe a cada 100 iterações
        print(f"Iteração {iter}: Melhor solução até o momento = {avaliar_custo(melhor_solucao, data_comum)}")

# Resultado final após as iterações
print(f"Solução final encontrada: {avaliar_custo(melhor_solucao, data_comum)}")
