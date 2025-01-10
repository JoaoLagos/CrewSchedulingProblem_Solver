class CommonDueDateSchedule:
    def __init__(self, caminho_arquivo: str):
        """
        Inicializa a classe CommonDueDateSchedule com os dados de um arquivo de texto.

        Args:
            caminho_arquivo (str): O caminho para o arquivo de texto contendo os dados dos problemas e trabalhos.
        """
        self.caminho_arquivo = caminho_arquivo
        self.problemas = {}  # Dicionário para armazenar os problemas com seus trabalhos
        self._carregar_dados()

    def _carregar_dados(self):
        """
        Método privado para carregar e analisar os dados do arquivo.
        """
        try:
            with open(self.caminho_arquivo, 'r') as arquivo:
                qtd_problemas = int(arquivo.readline().strip())  # Lê a quantidade de problemas
                for problema_idx in range(1, qtd_problemas + 1):
                    qtd_trabalhos = int(arquivo.readline().strip())  # Lê a quantidade de trabalhos para o problema atual
                    trabalhos = []
                    for _ in range(qtd_trabalhos):
                        tempo_processamento, custo_antecipado, custo_atraso = map(int, arquivo.readline().strip().split())
                        trabalhos.append({
                            'tempo_processamento': tempo_processamento,
                            'custo_antecipado': custo_antecipado,
                            'custo_atraso': custo_atraso
                        })
                    self.problemas[f'Problema {problema_idx}'] = trabalhos
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def definir_data_comum(self, problema: str, data: int):
        """
        Define uma data comum para todos os trabalhos de um problema específico.

        Args:
            problema (str): O nome do problema, e.g., 'Problema 1'.
            data (int): A data comum a ser aplicada.
        """
        self.problemas[problema]["data_comum"] = data

    def calcular_penalidades(self, problema: str, data_comum: int): #TODO: Ter bastante atenção!
        """
        Calcula as penalidades totais para um problema com base em uma data comum fornecida.

        Args:
            problema (str): O nome do problema.
            data_comum (int): A data comum para o problema.

        Returns:
            float: O custo total de penalidades para o problema.
        """
        trabalhos = self.problemas[problema]
        tempo_acumulado = 0
        penalidade_total = 0

        for trabalho in trabalhos:
            tempo_acumulado += trabalho['tempo_processamento']
            antecipacao = max(0, data_comum - tempo_acumulado)
            atraso = max(0, tempo_acumulado - data_comum)
            penalidade_antecipacao = antecipacao * trabalho['custo_antecipado']
            penalidade_atraso = atraso * trabalho['custo_atraso']
            penalidade_total += penalidade_antecipacao + penalidade_atraso

        return penalidade_total

    def exibir_informacoes(self):
        """
        Exibe um resumo das informações de todos os problemas e trabalhos.
        """
        print(f"Número de Problemas: {len(self.problemas)}")
        for problema, trabalhos in self.problemas.items():
            print(f"\n{problema}:")
            print(f"  Número de Trabalhos: {len(trabalhos)}")
            for i, trabalho in enumerate(trabalhos, 1):
                print(f"    Trabalho {i}: Tempo de Processamento={trabalho['tempo_processamento']}, "
                      f"Custo Antecipado={trabalho['custo_antecipado']}, Custo Atraso={trabalho['custo_atraso']}")
                
    def mostrar_problemas(self):
        print(self.problemas["Problema 3"])
