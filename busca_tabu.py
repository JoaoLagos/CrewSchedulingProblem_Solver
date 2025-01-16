
import copy
import random
from algoritmo_construtivo import AlgoritmoConstrutivo
from problema_sch.common_due_date_schedule import CommonDueDateSchedule

class TabuSearch:
    def __init__(self, agendamento, max_iteracoes=5000, tamanho_lista_tabu=10):
        """
        Inicializa a busca tabu para otimizar o agendamento de problemas com data comum de vencimento.

        Args:
            agendamento (CommonDueDateSchedule): Instância de agendamento com os problemas a serem resolvidos.
            max_iteracoes (int): Número máximo de iterações.
            tamanho_lista_tabu (int): Tamanho máximo da lista tabu.
        """
        self.agendamento = agendamento
        self.max_iteracoes = max_iteracoes
        self.tamanho_lista_tabu = tamanho_lista_tabu

    def gerar_movimento(self, s):
        """
        Gera um movimento aleatório a partir de uma solução atual.

        Args:
            s (list): Lista de trabalhos representando a solução atual.

        Returns:
            list: Nova solução após aplicar um movimento aleatório.
        """
        trabalhos = copy.deepcopy(s)
        i, j = random.sample(range(len(trabalhos)), 2)
        trabalhos[i], trabalhos[j] = trabalhos[j], trabalhos[i]
        return trabalhos

    def avaliar_custo(self, solucao, data_vencimento_comum): # Dentro tem o mesmo escopo que em Problema.calcular_penalidades()
        """
        Avalia o custo de penalidade de uma solução.

        Args:
            movimento (list): Solução representada como uma lista de trabalhos.
            data_vencimento_comum (float): Data de vencimento comum para o problema.

        Returns:
            float: Custo total de penalidade da solução.
        """
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
        Executa a busca tabu para um problema específico.

        Args:
            problema (Problema): Problema a ser resolvido.

        Returns:
            float: Custo da melhor solução encontrada.
            list: Melhor solução encontrada.
        """
        data_comum = problema.data_vencimento_comum
        s = AlgoritmoConstrutivo(problema).gerar_solucao_inicial() # Lista com a ordem de execução das tarefas/trabalhos (cronograma)
        melhor_solucao = copy.deepcopy(s)
        lista_tabu = []
        iter = 0
        #melhor_iter = 0

        while iter < self.max_iteracoes:
            iter += 1
            nova_solucao = self.gerar_movimento(melhor_solucao)
            if nova_solucao not in lista_tabu:
                custo_nova_solucao = self.avaliar_custo(nova_solucao, data_comum)
                custo_melhor_solucao = self.avaliar_custo(melhor_solucao, data_comum)
                if custo_nova_solucao < custo_melhor_solucao:
                    melhor_solucao = nova_solucao
                    #melhor_iter = iter
                    lista_tabu.append(nova_solucao)
                    if len(lista_tabu) > self.tamanho_lista_tabu:
                        lista_tabu.pop(0)

        return self.avaliar_custo(melhor_solucao, data_comum), melhor_solucao
