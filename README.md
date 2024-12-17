## Cleaner - Robô Aspirador Inteligente com IA

### Tecnologias Usadas:

- **Python**: A linguagem escolhida pela sua simplicidade e eficiência na implementação de algoritmos e resolução de problemas complexos.
- **Programação Orientada a Objetos (POO)**: Classes e objetos para representar o robô e o ambiente.
- **Algoritmos Autônomos**: Lógica de controle com base no estado das salas, utilizando técnicas de tomada de decisão.
- **Inteligência Artificial**: O projeto aplica métodos de **aprendizado supervisionado** e **não supervisionado** para otimizar a estratégia de limpeza do robô.

---

### Visão Geral do Projeto:

Este projeto simula o comportamento de um robô aspirador inteligente que pode se mover entre diversas salas e limpá-las com base em diferentes estratégias de controle. O robô pode operar em modo manual, onde o usuário comanda suas ações, ou em modo autônomo, onde o robô toma decisões baseadas nas sujeiras detectadas nas salas.

As funcionalidades impulsionadas por IA utilizam **aprendizado supervisionado** para reconhecer padrões de limpeza das salas e **aprendizado não supervisionado** para adaptar a abordagem de limpeza do robô com base nas condições ambientais e nas experiências anteriores.

**As estratégias de controle incluem**:
1. **Controle Base**: O robô segue um caminho predefinido limpando as salas com base na sua posição atual.
2. **Controle Manual**: O usuário controla diretamente os movimentos do robô.
3. **Controle Onisciente**: O robô sabe a posição de toda sujeira e escolhe a ordem ideal para limpar.

---

### Como Executar o Projeto:

**Pré-requisitos**:
- Certifique-se de que o **Python** esteja instalado em sua máquina. Caso contrário, baixe em [python.org](https://www.python.org/downloads/).

**Instalando o Projeto**:

1. Clone o repositório:
    ```bash
    git clone https://github.com/SeuUsername/RobôAspiradorInteligente.git
    cd RobôAspiradorInteligente
    ```

2. Execute o programa:
    ```bash
    python main.py
    ```

---

### Detalhamento da Lógica do Código:

#### **Cleaner.py**:
A classe `Cleaner` representa o robô aspirador, responsável por:
- Limpar a sala onde está localizado.
- Mover-se para a esquerda ou direita entre as salas.
- Verificar se a sala está suja.
- Atualizar sua memória, registrando as salas que limpou.

Métodos principais:
- `limpar(salas)`: Limpa a sala.
- `mover_direita(salas)`: Move o robô para a sala à direita.
- `mover_esquerda(salas)`: Move o robô para a sala à esquerda.
- `verifica_limpo(salas)`: Verifica se a sala está suja.
- `atualiza_memoria()`: Registra a sala limpa na memória do robô.

#### **Controlador.py**:
O controlador gerencia o movimento e a limpeza do robô com várias lógicas de controle:

1. **logica_robo_base**: O robô se move da esquerda para a direita, limpando as salas.
2. **logica_robo_onisciente**: O robô, sabendo a localização da sujeira, escolhe a ordem ideal de limpeza.
3. **manual_base**: O robô é controlado manualmente pelo usuário, com opções para mover, limpar ou parar o programa.
4. **Funções auxiliares**: Como `verifica_sujeira_longe`, que determina onde estão as sujeiras mais distantes.

#### **Funcionalidades de IA**:
- **Aprendizado Supervisionado**: O robô é treinado para reconhecer padrões de limpeza das salas (sujas ou limpas) e usar esses dados para melhorar suas estratégias de limpeza.
- **Aprendizado Não Supervisionado**: O robô adapta seu comportamento com base nas mudanças ambientais. Ele ajusta dinamicamente a ordem das tarefas de limpeza para minimizar o tempo e o consumo de energia, aprendendo com as sessões de limpeza anteriores.

---

### 👨‍💼 Autor

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://github.com/emiliobiasi.png" width="100px;" alt="Foto do Emílio no GitHub"/><br>
        <sub>
          <b>Emílio Biasi</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
