import random

lucro_dos_objetos = [24, 13, 23, 15, 16]
peso_dos_objetos = [12, 7, 11, 8, 9]
tamanho_da_mochila = 26
penalidade = 15


tamanho_da_solucao = len(lucro_dos_objetos)
tamanho_da_populacao = 4
quantidade_total_de_avaliacoes = 20
quantidade_atual_de_avaliacoes = 0
percentual_de_realizar_mutacao = 3 # 3% de chance de realizar a mutação
populacao = []
proxima_populacao = []
fitness = [0] * tamanho_da_populacao
fitness_proxima_populacao = [0] * (tamanho_da_populacao + 1)
indice_da_melhor_solucao = 0
indice_da_pior_solucao = 0

melhor_fitness_da_geracao = []
media_fitness_da_geracao = []
pior_fitness_da_geracao = []


def funcao_objetivo(solucao):
    fitness = 0
    peso = 0
    for i in range(len(solucao)):
        fitness = fitness + (solucao[i] * lucro_dos_objetos[i])
        peso = peso + (solucao[i] * peso_dos_objetos[i])

    if (peso > tamanho_da_mochila):
        fitness = fitness - penalidade

    return fitness


for i in range (tamanho_da_populacao):
    populacao.append([0] * tamanho_da_solucao)
    proxima_populacao.append([0] * tamanho_da_solucao)

proxima_populacao.append([0] * tamanho_da_solucao)

def avaliar_solucao(indice):
    fitness[indice] = funcao_objetivo(populacao[indice])

def avaliar_populacao():
    for i in range(tamanho_da_populacao):
        avaliar_solucao(i)

def identificar_melhor_solucao():
    indice_da_melhor_solucao = 0
    for i in range(tamanho_da_populacao):
        if fitness[indice_da_melhor_solucao] < fitness[i]:
            indice_da_melhor_solucao = i
    return indice_da_melhor_solucao

def elitismo():
    indice_da_melhor_solucao = identificar_melhor_solucao()
    proxima_populacao[tamanho_da_populacao] = populacao[indice_da_melhor_solucao]
    fitness_proxima_populacao[tamanho_da_populacao] = fitness[indice_da_melhor_solucao]

def mutacao(indice):
    for i in range(tamanho_da_solucao):
        if random.randint(0, 100) <= percentual_de_realizar_mutacao:
            if populacao[indice][i] == 0:
                proxima_populacao[indice][i] = 1
            else:
                proxima_populacao[indice][i] = 0
        else:
            proxima_populacao[indice][i] = populacao[indice][i]

def identificar_pior_solucao_da_proxima_populacao():
    indice_da_pior_solucao = 0
    for i in range(tamanho_da_populacao+1):
        if fitness_proxima_populacao[indice_da_pior_solucao] > fitness_proxima_populacao[i]:
            indice_da_pior_solucao = i
    return indice_da_pior_solucao

def gerar_solucao_inicial():
    for i in range(tamanho_da_populacao):
        for j in range(tamanho_da_solucao):
            populacao[i][j] = random.randint(0, 1)

def identificar_pior_solucao_da_populacao_atual():
    indice_da_pior_solucao = 0
    for i in range(tamanho_da_populacao):
        if fitness[indice_da_pior_solucao] > fitness[i]:
            indice_da_pior_solucao = i
    return indice_da_pior_solucao

def gerar_proxima_populacao():
    pior = identificar_pior_solucao_da_proxima_populacao()
    del proxima_populacao[pior]
    del fitness_proxima_populacao[pior]

    populacao = proxima_populacao
    fitness = fitness_proxima_populacao

    proxima_populacao.append(proxima_populacao[0])
    fitness_proxima_populacao.append(fitness_proxima_populacao[0])

def criterio_de_parada_atingido(quantidade_atual_de_avaliacoes):
    return quantidade_atual_de_avaliacoes >= quantidade_total_de_avaliacoes

def relatorio_de_convergencia_da_geracao():
    melhor_fitness_da_geracao.append(fitness[identificar_melhor_solucao()])
    pior_fitness_da_geracao.append(fitness[identificar_pior_solucao_da_populacao_atual()])
    media = 0
    for i in fitness:
        media = media+i
    media_fitness_da_geracao.append(media/len(fitness))

def startAlgoritm():
    gerar_solucao_inicial()
    avaliar_populacao()
    quantidade_atual_de_avaliacoes = tamanho_da_populacao
    relatorio_de_convergencia_da_geracao()
    contador = 0
    while not criterio_de_parada_atingido(quantidade_atual_de_avaliacoes):
        elitismo()
        for i in range(tamanho_da_populacao):
            mutacao(i)
            fitness_proxima_populacao[i] = funcao_objetivo(proxima_populacao[i])
            quantidade_atual_de_avaliacoes = quantidade_atual_de_avaliacoes + 1
        gerar_proxima_populacao()
        relatorio_de_convergencia_da_geracao()
        contador = contador + 1
    print("Melhor individuo")
    melhor_final = identificar_melhor_solucao()
    print(populacao[melhor_final])
    print("Fitness =",fitness[melhor_final])

do = 30
while do >= 0:
    startAlgoritm()
    do = do - 1