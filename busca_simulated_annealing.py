import copy
import random
import math
from algoritmo_construtivo import AlgoritmoConstrutivo
from problema_sch.common_due_date_schedule import CommonDueDateSchedule

class SimulatedAnnealing:
    def __init__(self, agendamento, temperatura_inicial=1000, taxa_resfriamento=0.995, iteracoes_por_temperatura=100):
        """
        Inicializa o algoritmo de Simulated Annealing para otimizar o agendamento de problemas com data comum de vencimento.

        Args:
            agendamento (CommonDueDateSchedule): Instância de agendamento com os problemas a serem resolvidos.
            temperatura_inicial (float): Temperatura inicial para o algoritmo.
            taxa_resfriamento (float): Taxa de resfriamento para a temperatura.
            iteracoes_por_temperatura (int): Número de iterações a serem realizadas por temperatura.
        """
        self.agendamento = agendamento
        self.temperatura_inicial = temperatura_inicial
        self.taxa_resfriamento = taxa_resfriamento
        self.iteracoes_por_temperatura = iteracoes_por_temperatura

    def gerar_movimento(self, s):
        # Implementação de um movimento aleatório, similar ao TabuSearch
        # Troca dois elementos aleatórios na solução
        nova_solucao = s[:]
        i, j = random.sample(range(len(s)), 2)
        nova_solucao[i], nova_solucao[j] = nova_solucao[j], nova_solucao[i]
        return nova_solucao

    def avaliar_custo(self, solucao, data_vencimento_comum):
        # Avalia o custo da solução, similar ao TabuSearch
        tempo_acumulado = 0
        penalidade_total = 0

        for trabalho in solucao:
            tempo_acumulado += trabalho.tempo_processamento
            if tempo_acumulado < data_vencimento_comum:
                penalidade = (data_vencimento_comum - tempo_acumulado) * trabalho.custo_antecipado
            elif tempo_acumulado > data_vencimento_comum:
                penalidade = (tempo_acumulado - data_vencimento_comum) * trabalho.custo_atraso
            else:
                penalidade = 0
            penalidade_total += penalidade

        return penalidade_total

    def executar(self, problema):
        """
        Executa o algoritmo de Simulated Annealing para um problema específico.

        Args:
            problema (Problema): Problema a ser resolvido.

        Returns:
            float: Custo da melhor solução encontrada.
            list: Melhor solução encontrada.
        """
        data_comum = problema.data_vencimento_comum
        s = AlgoritmoConstrutivo(problema).gerar_solucao_inicial()
        melhor_solucao = copy.deepcopy(s)
        custo_melhor_solucao = self.avaliar_custo(melhor_solucao, data_comum)

        temperatura = self.temperatura_inicial

        while temperatura > 1:
            for _ in range(self.iteracoes_por_temperatura):
                nova_solucao = self.gerar_movimento(melhor_solucao)
                custo_nova_solucao = self.avaliar_custo(nova_solucao, data_comum)

                if custo_nova_solucao < custo_melhor_solucao:
                    melhor_solucao = nova_solucao
                    custo_melhor_solucao = custo_nova_solucao
                else:
                    delta = custo_nova_solucao - custo_melhor_solucao
                    probabilidade_aceitacao = math.exp(-delta / temperatura)
                    if random.random() < probabilidade_aceitacao:
                        melhor_solucao = nova_solucao
                        custo_melhor_solucao = custo_nova_solucao

            temperatura *= self.taxa_resfriamento

        return custo_melhor_solucao, melhor_solucao 