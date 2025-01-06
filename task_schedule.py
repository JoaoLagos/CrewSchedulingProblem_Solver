class TaskSchedule:
    def __init__(self, path_arquivo):
        self.path_arquivo = path_arquivo
        self.num_tarefas = 0
        self.limite_tempo = 0
        self.tarefas = {}  # Dicionário para armazenar as tarefas como {número_da_tarefa: (inicio, fim)}
        self.transicoes = []  # Lista para armazenar as transições como tuplas (tarefa_i, tarefa_j, custo)
        self._carregar_dados()
    
    def _carregar_dados(self):
        """Método privado para ler e analisar os dados do arquivo."""
        try:
            with open(self.path_arquivo, 'r') as arquivo:
                # Ler a primeira linha para obter o número de tarefas e o limite de tempo
                self.num_tarefas, self.limite_tempo = map(int, arquivo.readline().strip().split())
                
                # Ler as próximas linhas para obter as tarefas
                for i in range(1, self.num_tarefas + 1):
                    inicio, fim = map(int, arquivo.readline().strip().split())
                    self.tarefas[i] = (inicio, fim)
                
                # Ler as linhas restantes para obter as transições
                for linha in arquivo:
                    tarefa_i, tarefa_j, custo = map(int, linha.strip().split())
                    self.transicoes.append((tarefa_i, tarefa_j, custo))
        except Exception as e:
            print(f"Erro ao ler/analisar o arquivo: {e}")

    def obter_tarefas(self):
        """Retorna o dicionário de tarefas."""
        return self.tarefas

    def obter_transicoes(self):
        """Retorna a lista de transições."""
        return self.transicoes

    def exibir_informacoes(self):
        """Exibe um resumo das informações do agendamento."""
        print(f"Número de Tarefas: {self.num_tarefas}")
        print(f"Limite de Tempo: {self.limite_tempo}")
        print("Tarefas (Número: Início, Fim):")
        for numero, tarefa in self.tarefas.items():
            print(f"Tarefa {numero}: {tarefa}")
        print("Transições (Tarefa_i, Tarefa_j, Custo):")
        for transicao in self.transicoes:
            print(transicao)
