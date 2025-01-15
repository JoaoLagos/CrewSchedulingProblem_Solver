class CommonDueDateSchedule:
    def __init__(self, caminho_arquivo: str, param_h: float):
        """
        Inicializa a classe CommonDueDateSchedule com os dados de um arquivo de texto.

        Args:
            caminho_arquivo (str): O caminho para o arquivo de texto contendo os dados dos problemas e trabalhos.
        """
        self.caminho_arquivo = caminho_arquivo
        self.param_h = param_h
        self.problemas = []  # Lista de objetos Problema
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
                    problema = Problema(f"Problema {problema_idx}", param_h=self.param_h)  
                    for _ in range(qtd_trabalhos):
                        tempo_processamento, custo_antecipado, custo_atraso = map(int, arquivo.readline().strip().split())
                        problema.adicionar_trabalho(tempo_processamento, custo_antecipado, custo_atraso) # Adiciona o trabalho com sua respectiva informação
                    problema.definir_data_comum() # Calcula a data comum
                    self.problemas.append(problema)
                    
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def calcular_penalidades_para_problema(self, indice_problema: int):
        """
        Calcula as penalidades totais para um problema com base na data comum definida.

        Args:
            indice_problema (int): O índice do problema na lista (baseado em 1).

        Returns:
            float: O custo total de penalidades para o problema.
        """
        return self.problemas[indice_problema - 1].calcular_penalidades()

    def exibir_informacoes(self):
        """
        Exibe um resumo das informações de todos os problemas e trabalhos.
        """
        print(f"Número de Problemas: {len(self.problemas)}")
        for problema in self.problemas:
            problema.exibir_informacoes()

class Problema:
    def __init__(self, nome, param_h):
        """
        Inicializa uma instância de um problema com uma lista de trabalhos.

        Args:
            nome (str): Nome do problema, e.g., 'Problema 1'.
            param_h (int): Parâmetro específico para o problema (se necessário).
        """
        self.nome = nome
        self.param_h = param_h
        self.trabalhos = []  # Lista para armazenar os trabalhos
        self.data_vencimento_comum = None
        self.tempo_acumulado = 0 # Tempo Atual
        self.penalidade_total = 0

    def adicionar_trabalho(self, tempo_processamento, custo_antecipado, custo_atraso):
        """
        Adiciona um trabalho à lista de trabalhos do problema.

        Args:
            tempo_processamento (int): Tempo de processamento do trabalho.
            custo_antecipado (int): Custo por antecipação.
            custo_atraso (int): Custo por atraso.
        """
        self.trabalhos.append({
            'tempo_processamento': tempo_processamento,
            'custo_antecipado': custo_antecipado,
            'custo_atraso': custo_atraso
        })

    def definir_data_comum(self):
        """
        Define uma data de vencimento comum para o problema com base na soma dos tempos de processamento e o parâmetro h.
        """
        soma_p = sum(trabalho['tempo_processamento'] for trabalho in self.trabalhos)
        self.data_vencimento_comum = soma_p * self.param_h

    def calcular_penalidades(self):
        """
        Calcula as penalidades totais com base na data de vencimento comum definida.

        Returns:
            float: O custo total de penalidades.
        """
        if self.data_vencimento_comum is None:
            raise ValueError("Data de vencimento comum não definida.")

        for trabalho in self.trabalhos:
            self.tempo_acumulado += trabalho['tempo_processamento']

            # Calculando as penalidades diretamente
            if self.tempo_acumulado < self.data_vencimento_comum:  # Antecipação
                penalidade = (self.data_vencimento_comum - self.tempo_acumulado) * trabalho['custo_antecipado']
            elif self.tempo_acumulado > self.data_vencimento_comum:  # Atraso
                penalidade = (self.tempo_acumulado - self.data_vencimento_comum) * trabalho['custo_atraso']
            else:  # Nenhuma penalidade, caso não haja antecipação nem atraso, ou seja, tempo de término do trabalho é EXATAMENTE IGUAL ao vencimento_comum
                penalidade = 0

            # Somando a penalidade total
            self.penalidade_total += penalidade

        return self.penalidade_total

    def exibir_informacoes(self):
        """
        Exibe informações detalhadas sobre o problema e seus trabalhos.
        """
        print(f"{self.nome}: Param_h={self.param_h}, Data de Vencimento Comum={self.data_vencimento_comum}")
        print(f"  Número de Trabalhos: {len(self.trabalhos)}")
        for i, trabalho in enumerate(self.trabalhos, 1):
            print(f"    Trabalho {i}: Tempo de Processamento={trabalho['tempo_processamento']}, "
                  f"Custo Antecipado={trabalho['custo_antecipado']}, Custo Atraso={trabalho['custo_atraso']}")
