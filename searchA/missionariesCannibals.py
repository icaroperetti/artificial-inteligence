import math

# 0 - 3 Missionários lado esquerdo
# 1 - 3 Canibais do lado esquerdo
# 2 - 0 Missionários do lado direito
# 3 - 0 Canibais lado direito
# 4 - Lado da canoa 0 - Esq - 1 Dir
initial_state = [3, 3, 0, 0, 0]


final_state = [0, 0, 3, 3, 1]

# [0] - Missionários e [1] - Canibais
movement_opt = [
    [1, 0], [1, 1], [0, 2], [2, 0], [0, 1]
]


# repeatedMovements = []


path = []


# Vetor para armazenar estados válidos
valid_states = []


def move(state, move):

    # O arr[-1] retorna sempre o ultimo elemento do vetor (direção)
    if state[-1] == 0:  # Direção para esquerda (0)
        # print(move)
        leftMiss = state[0] - move[0]
        rightMiss = state[2] + move[0]

        leftCann = state[1] - move[1]
        rightCann = state[3] + move[1]

        # Cria o estado filho
        children = [leftMiss, leftCann, rightMiss, rightCann, 1]

    else:  # Direção para direita (1)
        leftMiss = state[0] + move[0]

        rightMiss = state[2] - move[0]

        leftCann = state[1] + move[1]

        rightCann = state[3] - move[1]

        children = [leftMiss, leftCann, rightMiss, rightCann, 0]

    # Verifica se o estado é valido e se ele já não esta na lista de estados válidos
    if validState(children) and children not in valid_states:
        valid_states.append(children)
        return children


def validState(state):
    # Evitar negativos
    for i in range(len(state)):
        if state[i] < 0:
            return False

    # Não permitir mais canibais que missionários
    if ((state[0] == 0 or state[0] >= state[1]) and (state[2] == 0 or state[2] >= state[3])):
        return True


def euclidianDistance(initial_state, valid_state):
    # for state in valid_state:
    # Função da lib math que realiza cálculo euclidiano
    return math.dist(initial_state, valid_state)


def execute(state):
    movements = []
    minValue = 0
    minState = []
    distanceMinVal = 0

    # Se o estado for o estado final, encerra e retorna
    if state == final_state:
        print(f"SOLUÇÃO ENCONTRADA")
        print("Missionário Esquerda - Canibal Esquerda - Missionário Direita - Canibal Direita - Canoa")
        print('\n'.join('{}: {}'.format(*val) for val in enumerate(path)))
        return True

    # Realiza as movimentações de acordo com as regras
    for opt in movement_opt:
        movement = move(state, opt)  # Irá retornar somente estados válidos
        if movement:
            movements.append(movement)

    # Se não houverem movimentos possíveis,  executa a função novamente com o último estado válido
    if not movements:
        execute(valid_states[-1])
        return

    # Se houver movimentos possíveis, calcula a distância euclidiana entre o estado atual e cada movimento possível
    for i in range(len(movements)):
        distanceH = euclidianDistance(
            state, movements[i]) + distanceMinVal
        distanceG = euclidianDistance(final_state, movements[i])
        totalDist = distanceH + distanceG

        # Se o movimento for o primeiro, armazena o valor e o estado
        if i == 0:
            minValue = totalDist
            minState = movements[i]

        # Verifica se o valor atual é menor que o valor armazenado inicialmente
        if totalDist < minValue:
            minValue = totalDist
            minState = movements[i]

    # Armazena a distância já percorrida para utilizar na soma do distanceH
    # Inicialmente é 0, pois o estado inicial não tem distância percorrida
    distanceMinVal = distanceH

    # Adiciona o estado na lista de caminhos percorridos
    path.append(minState)

    # Chama a função recursiva para executar o algoritmo novamente
    execute(minState)
    return True


# Chamada da função passando o estado inicial
execute(initial_state)
