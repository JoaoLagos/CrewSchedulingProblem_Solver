# Um algoritmo construtivo visa construir uma possível solução inicial

import random


class AlgoritmoConstrutivo():
    def __init__(self, problema):
        """
        Inicializa a classe AlgoritmoConstrutivo com um problema.

        Args:
            problema (Problema): O problema a ser resolvido.
        """
        self.problema = problema

    def gerar_solucao_inicial(self):
        # Ordena os trabalhos com base no tempo de processamento em ordem crescente (menor para maior)
        #return list(self.problema.trabalhos.sort(key=lambda trabalho: (trabalho.tempo_processamento, trabalho.custo_antecipado, trabalho.custo_atraso)))
        #return list(self.problema.trabalhos)
        
        return sorted(self.problema.trabalhos, key=lambda trabalho: (trabalho.tempo_processamento, trabalho.custo_antecipado, trabalho.custo_atraso))

    
    def exibir_resultado(self):
        """
        Exibe a solução encontrada, com a ordem dos trabalhos e a penalidade total.
        """
        print(f"Agendamento dos trabalhos para o {self.problema.nome}:")
        for trabalho in self.problema.trabalhos:
            print(f"  {trabalho.nome}: Tempo de Processamento={trabalho.tempo_processamento}")
        
        # Exibe a penalidade total
        penalidade_total = self.problema.calcular_penalidades()
        print(f"Penalidade Total: {penalidade_total}")
        
