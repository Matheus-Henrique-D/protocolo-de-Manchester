# protocolo-de-Manchester

# 🏥 Simulador do Protocolo de Manchester

Este projeto é um simulador em Python de um sistema de triagem de pacientes, baseado no Protocolo de Manchester. [cite_start]Foi desenvolvido como a Segunda Avaliação da disciplina de Estrutura de Dados da Fatec Rio Claro[cite: 2, 3, 4].

O objetivo do sistema é classificar pacientes por nível de urgência, inseri-los em filas de prioridade e chamar o paciente mais urgente para o atendimento.

## ✨ Funcionalidades

[cite_start]O sistema opera em um loop de menu contínuo e oferece as seguintes operações[cite: 21, 28]:

* **1. [cite_start]Cadastrar paciente:** Inicia o processo de triagem (árvore de decisão) e insere o paciente na fila correta [cite: 22-24].
* **2. [cite_start]Chamar paciente:** Remove e exibe o próximo paciente da fila de maior prioridade disponível (Vermelho > Laranja > Amarelo > Verde > Azul)[cite: 25].
* **3. [cite_start]Mostrar status:** Exibe o número de pacientes aguardando em cada uma das 5 filas[cite: 26].
* **0. [cite_start]Sair:** Encerra o programa[cite: 27].

## 🧠 Como Funciona

[cite_start]Para facilitar o entendimento por pessoas que não são da área de Estrutura de Dados [cite: 96-97], a lógica do sistema é dividida em duas partes principais:

### 1. A Triagem (Árvore de Decisão)

Quando um novo paciente é cadastrado, o sistema precisa decidir sua urgência. [cite_start]Isso é feito através de uma **Árvore de Decisão**[cite: 7]. Pense nela como um fluxograma de perguntas "sim" ou "não":

* [cite_start]Cada pergunta é um **"Nó"** na árvore[cite: 8].
* Dependendo da resposta (`s` ou `n`), o sistema segue para um "galho" diferente: ou outra pergunta, ou um resultado final.
* [cite_start]O resultado final é a **Cor** da classificação (o nó "folha")[cite: 9].

[cite_start]A lógica de decisão implementada neste projeto segue a sugestão simplificada fornecida[cite: 63]:
1.  [cite_start]`"Está respirando?"` [cite: 64]
    * [cite_start]Não $\rightarrow$ **Vermelho** [cite: 65]
    * [cite_start]Sim $\rightarrow$ 2. `"Está consciente?"` [cite: 66]
        * [cite_start]Não $\rightarrow$ **Laranja** [cite: 67, 69]
        * [cite_start]Sim $\rightarrow$ 3. `"Está com dor intensa?"` [cite: 68]
            * [cite_start]Sim $\rightarrow$ **Amarelo** [cite: 70, 71]
            * [cite_start]Não $\rightarrow$ **Verde** [cite: 72, 73]

### 2. As Filas de Prioridade (FIFO)

Após receber uma cor na triagem, o paciente é enviado para uma sala de espera. [cite_start]No nosso sistema, temos **5 filas de espera separadas**, uma para cada cor[cite: 19].

* [cite_start]🔴 **Vermelho:** Emergência [cite: 10, 11]
* [cite_start]🟠 **Laranja:** Muito urgente [cite: 12]
* [cite_start]🟡 **Amarelo:** Urgente [cite: 13, 14]
* [cite_start]🟢 **Verde:** Pouco urgente [cite: 15, 16]
* [cite_start]🔵 **Azul:** Não urgente [cite: 17, 18]

O sistema gerencia essas filas da seguinte forma:
1.  [cite_start]**FIFO:** Cada fila individual respeita a ordem de chegada (Primeiro a Entrar, Primeiro a Sair)[cite: 20].
2.  **Prioridade:** Quando um médico chama o próximo paciente (Opção 2), o sistema **sempre** verifica a fila Vermelha primeiro. Somente se ela estiver vazia, ele olha para a Laranja. [cite_start]Se a Laranja estiver vazia, ele olha para a Amarela, e assim por diante[cite: 25].

## 📁 Estrutura do Projeto

O código foi separado em dois arquivos principais para melhor organização:

* [cite_start]`main.py`: Contém a interface do usuário (o `menu_interativo`) e o loop principal que executa o programa[cite: 62].
* `backend.py`: Contém toda a lógica e as estruturas de dados:
    * [cite_start]`Classe Fila`: Implementação da fila FIFO[cite: 59].
    * [cite_start]`Classe NodoArvore`: Estrutura para os nós da árvore de decisão[cite: 58].
    * `Classe Paciente`: (Classe auxiliar) Armazena os dados do paciente.
    * `Classe SistemaTriagem`: (Classe auxiliar) Orquestra toda a lógica, gerenciando as filas e o processo de triagem.

## 🚀 Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Clone este repositório:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    ```
3.  Navegue até a pasta do projeto:
    ```bash
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
4.  Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```
5.  O menu interativo será iniciado no seu terminal.