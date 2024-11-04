import random
import math
import matplotlib.pyplot as plt

# Dados do problema: valores e pesos dos itens e capacidade da mochila
valores = [60, 100, 120, 90, 50, 70, 30, 80, 110, 40, 95, 85, 55, 65, 75]  # Valores dos itens
pesos = [10, 20, 30, 15, 25, 35, 10, 20, 40, 15, 25, 18, 28, 22, 12]      # Pesos dos itens
capacidade = 100                                           # Capacidade máxima da mochila
n = len(valores)                                           # Número de itens


# Parâmetros da Têmpera Simulada
temperatura_inicial = 1000
temperatura_final = 1e-3
fator_resfriamento = 0.95
max_iteracoes = 1000

# Função de cálculo de valor da mochila
def calcular_valor(solucao):
    valor_total = sum(valores[i] * solucao[i] for i in range(n))
    peso_total = sum(pesos[i] * solucao[i] for i in range(n))
    if peso_total > capacidade:
        return 0  # Penaliza soluções inválidas
    return valor_total

# Função de Têmpera Simulada
def tempera_simulada():
    # Solução inicial aleatória
    solucao = [random.randint(0, 1) for _ in range(n)]
    valor_atual = calcular_valor(solucao)
    melhor_valor = valor_atual
    melhor_ciclo = 0
    temperatura = temperatura_inicial

    for ciclo in range(max_iteracoes):
        # Gera uma solução vizinha aleatória
        vizinho = solucao[:]
        i = random.randint(0, n - 1)
        vizinho[i] = 1 - vizinho[i]  # Inverte o item
        valor_vizinho = calcular_valor(vizinho)

        # Aceita ou rejeita o vizinho
        delta = valor_vizinho - valor_atual
        if delta > 0 or random.random() < math.exp(delta / temperatura):
            solucao = vizinho
            valor_atual = valor_vizinho

        # Atualiza o melhor valor e o ciclo do melhor valor
        if valor_atual > melhor_valor:
            melhor_valor = valor_atual
            melhor_ciclo = ciclo

        # Resfriamento
        temperatura *= fator_resfriamento
        if temperatura < temperatura_final:
            break

    return melhor_valor, melhor_ciclo, valor_atual

# Executa o algoritmo 100 vezes e coleta os resultados
melhores_valores = []
ciclos_melhores = []
ultimos_valores = []

for _ in range(100):
    melhor_valor, melhor_ciclo, ultimo_valor = tempera_simulada()
    melhores_valores.append(melhor_valor)
    ciclos_melhores.append(melhor_ciclo)
    ultimos_valores.append(ultimo_valor)

# Gera os histogramas
plt.figure(figsize=(15, 5))

# Histograma dos Melhores Valores
plt.subplot(1, 3, 1)
plt.hist(melhores_valores, bins=10, color='blue', edgecolor='black')
plt.title("Histograma dos Melhores Valores")
plt.xlabel("Melhor Valor")
plt.ylabel("Frequência")

# Histograma dos Ciclos do Melhor Valor
plt.subplot(1, 3, 2)
plt.hist(ciclos_melhores, bins=10, color='green', edgecolor='black')
plt.title("Histograma dos Ciclos do Melhor Valor")
plt.xlabel("Ciclo do Melhor Valor")
plt.ylabel("Frequência")

# Histograma dos Últimos Valores
plt.subplot(1, 3, 3)
plt.hist(ultimos_valores, bins=10, color='red', edgecolor='black')
plt.title("Histograma dos Últimos Valores")
plt.xlabel("Último Valor")
plt.ylabel("Frequência")

plt.tight_layout()
plt.show()
