import random
import numpy as np


NB_TACHES = 10
DISTANCES = np.array([
    [0, 2, 9, 10, 7, 3, 8, 6, 4, 9],
    [2, 0, 5, 6, 4, 9, 3, 7, 8, 2],
    [9, 5, 0, 3, 8, 7, 4, 2, 6, 9],
    [10, 6, 3, 0, 9, 4, 5, 8, 7, 3],
    [7, 4, 8, 9, 0, 5, 6, 3, 2, 8],
    [3, 9, 7, 4, 5, 0, 2, 8, 6, 9],
    [8, 3, 4, 5, 6, 2, 0, 9, 7, 1],
    [6, 7, 2, 8, 3, 8, 9, 0, 5, 2],
    [4, 8, 6, 7, 2, 6, 7, 5, 0, 3],
    [9, 2, 9, 3, 8, 9, 1, 2, 3, 0]
])

POPULATION_SIZE = 80
NB_GENERATIONS = 100
MUTATION_RATE = 0.3




def cout(solution):
    return sum(DISTANCES[solution[i], solution[i + 1]] for i in range(len(solution) - 1))


def selection_par_rang(population):
    population = sorted(population, key=cout)
    ranks = np.arange(1, len(population) + 1)
    probabilities = ranks / ranks.sum()
    return random.choices(population, weights=probabilities, k=2)


def croisement_simple(parent1, parent2):
    point = random.randint(1, NB_TACHES - 2)
    child = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]
    return child


def croisement_double(parent1, parent2):
    p1, p2 = sorted(random.sample(range(NB_TACHES), 2))
    segment = parent1[p1:p2]
    child = [x for x in parent2 if x not in segment]
    return child[:p1] + segment + child[p1:]


def croisement_uniforme(parent1, parent2):
    child = []
    for i in range(NB_TACHES):
        if random.random() < 0.5:
            gene = parent1[i]
        else:
            gene = parent2[i]
        if gene not in child:
            child.append(gene)
    for gene in range(NB_TACHES):
        if gene not in child:
            child.append(gene)
    return child


def mutation(solution):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NB_TACHES), 2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution


def algo_genetique_rang(croisement_fonction, nom_croisement):
    population = [random.sample(range(NB_TACHES), NB_TACHES) for _ in range(POPULATION_SIZE)]

    for gen in range(NB_GENERATIONS):
        nouvelle_pop = []
        for _ in range(POPULATION_SIZE // 2):
            p1, p2 = selection_par_rang(population)
            enfant1 = mutation(croisement_fonction(p1, p2))
            enfant2 = mutation(croisement_fonction(p2, p1))
            nouvelle_pop.extend([enfant1, enfant2])
        population = nouvelle_pop

    meilleur = min(population, key=cout)
    print(f"\n--- Résultat avec {nom_croisement} ---")
    print(f"Meilleure solution trouvée: {meilleur}")
    print(f"Distance minimale: {cout(meilleur)}")




print("Lancement de l'algorithme génétique avec SÉLECTION PAR RANG...")

algo_genetique_rang(croisement_simple, "Croisement Simple Ordonné")
algo_genetique_rang(croisement_double, "Croisement Double Ordonné")
algo_genetique_rang(croisement_uniforme, "Croisement Uniforme")
