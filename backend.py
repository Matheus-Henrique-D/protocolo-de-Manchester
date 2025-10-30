class paciente:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return f"{self.nome} - {self.codigo}"


class fila:
    class No:
        def __init__(self, valor):
            self.valor = valor
            self.proximo = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.quantidade = 0

    # Método que retorna a quantidade de elementos
    def __len__(self):
        return self.quantidade

    def __iter__(self):
        atual = self.head
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __str__(self):
        return '[' + ', '.join([str(valor) for valor in self]) + ']'

    def esta_vazia(self):
        return self.head is None

    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.quantidade += 1

        # Quando a lista é vazia
        if self.head is None:
            self.head = novo
            self.tail = novo
            return
        # Quando a lista não é vazia
        self.tail.proximo = novo
        self.tail = novo

    def remover_inicio(self):
        if self.head is None:
            return None

        valor = self.head.valor
        self.head = self.head.proximo
        self.quantidade -= 1

        if self.head is None:
            self.tail = None

        return valor


class nodoarvore:
    def __init__(self, pergunta=None, resultado=None, escolha_sim=None, escolha_nao=None):
        self.pergunta = pergunta
        self.escolha_sim = escolha_sim
        self.escolha_nao = escolha_nao
        self.resultado = resultado

    @staticmethod
    def montando_as_decisoes():
        # Definindo os códigos de cores finais
        codigo_vermelho = nodoarvore(resultado="Vermelho - Emergência")
        codigo_laranja = nodoarvore(resultado="Laranja - Muito urgente")
        codigo_amarelo = nodoarvore(resultado="Amarelo - Urgente")
        codigo_verde = nodoarvore(resultado="Verde - Pouco urgente")
        codigo_azul = nodoarvore(resultado="Azul - não urgente")

        pergunta_final = nodoarvore(
            pergunta="Possui alguma dor crônica ou pode esperar até atendimento?",
            escolha_sim=codigo_azul,
            escolha_nao=codigo_verde
        )

        pergunta_4 = nodoarvore(
            pergunta="Está sentindo febre ou algum sintoma de mal estar?",
            escolha_sim=codigo_verde,
            escolha_nao=pergunta_final
        )

        pergunta_3 = nodoarvore(
            pergunta="Você está com dor intensa?",
            escolha_sim=codigo_amarelo,
            escolha_nao=pergunta_4
        )

        pergunta_2 = nodoarvore(
            pergunta="Você está consciente?",
            escolha_sim=pergunta_3,
            escolha_nao=codigo_laranja
        )

        pergunta_inicial = nodoarvore(
            pergunta="Você está respirando?",
            escolha_sim=pergunta_2,
            escolha_nao=codigo_vermelho
        )
        # Chama a pergunta inicial e percore todas se necessario.
        return pergunta_inicial

    @staticmethod
    def tomada_decisao(nodo_atual):
        # Se a informação é none ele retorna o resultado
        if nodo_atual.pergunta is None:
            return nodo_atual.resultado

        print(f"\nPergunta: {nodo_atual.pergunta}")


        while True:
            resposta = input("Responda com Sim(s) ou Não(n): ").strip().lower()
            if resposta == 's':
                return nodoarvore.tomada_decisao(
                    nodo_atual.escolha_sim)  # chama a classe e a função percorrendo as listas de escolhas
            elif resposta == 'n':
                return nodoarvore.tomada_decisao(nodo_atual.escolha_nao)
            else:
                print("Caracter inválido ou errado. Tente novamente.")


class SistemaTriagem:
    def __init__(self):
        # Dicionário de filas separadas por cor de prioridade
        self.filas = {
            "Vermelho - Emergência": fila(),
            "Laranja - Muito urgente": fila(),
            "Amarelo - Urgente": fila(),
            "Verde - Pouco urgente": fila(),
            "Azul - não urgente": fila()
        }

        # Emojis correspondentes a cada cor
        self.emojis = {
            "Vermelho - Emergência": "🔴",
            "Laranja - Muito urgente": "🟠",
            "Amarelo - Urgente": "🟡",
            "Verde - Pouco urgente": "🟢",
            "Azul - não urgente": "🔵"
        }

        # Ordem de prioridade (do mais urgente para o menos urgente)
        self.prioridades = [
            "Vermelho - Emergência",
            "Laranja - Muito urgente",
            "Amarelo - Urgente",
            "Verde - Pouco urgente",
            "Azul - não urgente"
        ]

    def cadastrar_paciente(self):
        """Cadastra um novo paciente através da triagem"""
        nome = input("Nome do paciente: ")

        # Monta a árvore de decisão
        arvore = nodoarvore.montando_as_decisoes()

        # Realiza a triagem
        codigo = nodoarvore.tomada_decisao(arvore)

        # Cria o paciente
        novo_paciente = paciente(nome, codigo)

        # Adiciona na fila correspondente
        self.filas[codigo].inserir_no_fim(novo_paciente)

        emoji = self.emojis[codigo]
        print(f"\nCor atribuída: {codigo} {emoji}")
        print(f"Paciente {nome} adicionado à fila {codigo.split(' - ')[0].lower()}.")

    def chamar_paciente(self):
        """Chama o próximo paciente da fila mais urgente"""
        # Percorre as filas por ordem de prioridade
        for prioridade in self.prioridades:
            if not self.filas[prioridade].esta_vazia():
                paciente_chamado = self.filas[prioridade].remover_inicio()
                emoji = self.emojis[prioridade]
                cor = prioridade.split(' - ')[0]
                print(f"\nChamando paciente da fila {cor}: {paciente_chamado.nome} {emoji}")
                return

        print("\n[AVISO] Não há pacientes nas filas!")

    def mostrar_status(self):
        """Mostra o status de todas as filas"""
        print("\n=== STATUS DAS FILAS ===")
        for prioridade in self.prioridades:
            tamanho = len(self.filas[prioridade])
            emoji = self.emojis[prioridade]
            cor = prioridade.split(' - ')[0]
            print(f"{emoji} {cor}: {tamanho} paciente(s)")