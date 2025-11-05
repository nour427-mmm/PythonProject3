import random
import numpy as np

tasks = [4, 3, 7, 2, 5, 6]

def evaluate(solution):
    total = 0
    current = 0
    for t in solution:
        current += tasks[t]
        total += current
    return total

def selection_roulette(pop, fitness):
    inv = [1 / f for f in fitness]
    total = sum(inv)
    probs = [v / total for v in inv]
    chosen = np.random.choice(len(pop), size=2, replace=False, p=probs)
    return pop[chosen[0]], pop[chosen[1]]

def crossover(p1, p2):
    a, b = sorted(random.sample(range(len(p1)), 2))
    child = [None] * len(p1)
    child[a:b] = p1[a:b]
    fill = [x for x in p2 if x not in child]
    j = 0
    for i in range(len(p1)):
        if child[i] is None:
            child[i] = fill[j]
            j += 1
    return child

def mutate(sol, rate=0.3):
    s = sol[:]
    if random.random() < rate:
        i, j = random.sample(range(len(s)), 2)
        s[i], s[j] = s[j], s[i]
    return s

def genetic_algorithm_roulette(pop_size=40, generations=100, crossover_rate=0.9, mutation_rate=0.3):
    pop = [random.sample(range(len(tasks)), len(tasks)) for _ in range(pop_size)]
    best_sol = None
    best_cost = float("inf")

    for gen in range(generations):
        fitness = [evaluate(ind) for ind in pop]
        gen_best_idx = np.argmin(fitness)
        gen_best_cost = fitness[gen_best_idx]

        if gen_best_cost < best_cost:
            best_cost = gen_best_cost
            best_sol = pop[gen_best_idx]
            print(f"[Génétique-Roulette] Génération {gen + 1}: meilleur coût = {best_cost}")

        new_pop = []
        for _ in range(pop_size // 2):
            p1, p2 = selection_roulette(pop, fitness)
            if random.random() < crossover_rate:
                c1 = crossover(p1, p2)
                c2 = crossover(p2, p1)
            else:
                c1, c2 = p1[:], p2[:]
            c1 = mutate(c1, mutation_rate)
            c2 = mutate(c2, mutation_rate)
            new_pop.extend([c1, c2])
        pop = new_pop

    return best_sol, best_cost

if __name__ == "__main__":
    sol, cost = genetic_algorithm_roulette()
    print(f" Solution finale Génétique (Roulette) : {sol} | Coût = {cost}")
