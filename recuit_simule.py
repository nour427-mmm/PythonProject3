import random
import math

tasks = [4, 3, 7, 2, 5, 6]

def evaluate(solution):
    total = 0
    current = 0
    for t in solution:
        current += tasks[t]
        total += current
    return total

def simulated_annealing(T_init=100, alpha=0.95, max_iter=200):
    current = random.sample(range(len(tasks)), len(tasks))
    best = current[:]
    best_cost = evaluate(best)
    T = T_init

    for it in range(max_iter):
        i, j = random.sample(range(len(tasks)), 2)
        neighbor = current[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        cost_current = evaluate(current)
        cost_neighbor = evaluate(neighbor)
        delta = cost_neighbor - cost_current

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbor[:]
            if cost_neighbor < best_cost:
                best, best_cost = neighbor[:], cost_neighbor
                print(f"[Recuit] Itération {it + 1}: meilleur coût = {best_cost}")

        T *= alpha

    return best, best_cost

if __name__ == "__main__":
    sol, cost = simulated_annealing()
    print(f"✅ Solution finale Recuit simulé : {sol} | Coût = {cost}")
