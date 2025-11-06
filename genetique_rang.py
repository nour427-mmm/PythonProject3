import random
import numpy as np


tasks = [4, 3, 7, 2, 5, 6, 8, 5, 9, 4]
NB_TACHES = len(tasks)
POPULATION_SIZE = 80
NB_GENERATIONS = 100
MUTATION_RATE = 0.3


def evaluate(solution):
    total, current = 0, 0
    for t in solution:
        current += tasks[t]
        total += current
    return total

def selection_rang(population):
    population = sorted(population, key=evaluate)
    ranks = np.arange(1, len(population) + 1)
    probs = ranks / ranks.sum()
    return random.choices(population, weights=probs, k=2)

def croisement_simple(p1, p2):
    point = random.randint(1, NB_TACHES - 2)
    return p1[:point] + [x for x in p2 if x not in p1[:point]]

def croisement_double(p1, p2):
    a, b = sorted(random.sample(range(NB_TACHES), 2))
    seg = p1[a:b]
    child = [x for x in p2 if x not in seg]
    return child[:a] + seg + child[a:]

def croisement_uniforme(p1, p2):
    child = []
    for i in range(NB_TACHES):
        gene = p1[i] if random.random() < 0.5 else p2[i]
        if gene not in child:
            child.append(gene)
    for g in range(NB_TACHES):
        if g not in child:
            child.append(g)
    return child

def mutation(sol):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NB_TACHES), 2)
        sol[i], sol[j] = sol[j], sol[i]
    return sol

def algo_genetique_rang(croisement, nom_croisement):
    population = [random.sample(range(NB_TACHES), NB_TACHES) for _ in range(POPULATION_SIZE)]
    best = min(population, key=evaluate)
    best_cost = evaluate(best)

    for gen in range(NB_GENERATIONS):
        new_pop = []
        for _ in range(POPULATION_SIZE // 2):
            p1, p2 = selection_rang(population)
            e1 = mutation(croisement(p1, p2))
            e2 = mutation(croisement(p2, p1))
            new_pop += [e1, e2]
        population = new_pop

        cur_best = min(population, key=evaluate)
        if evaluate(cur_best) < best_cost:
            best, best_cost = cur_best, evaluate(cur_best)
            print(f"[Rang] {nom_croisement} Génération {gen + 1}: coût = {best_cost}")

    print(f"\n Résultat final ({nom_croisement})")
    print(f"Solution : {best}")
    print(f"Coût minimal : {best_cost}\n")

if __name__ == "__main__":
    print("===  ALG. GÉNÉTIQUE – SÉLECTION PAR RANG ===")
    algo_genetique_rang(croisement_simple, "Croisement Simple")
    algo_genetique_rang(croisement_double, "Croisement Double")
    algo_genetique_rang(croisement_uniforme, "Croisement Uniforme")
