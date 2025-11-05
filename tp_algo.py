import random

tasks = [4, 3, 7, 2, 5, 6]

def evaluate(solution):
    total = 0
    current = 0
    for t in solution:
        current += tasks[t]
        total += current
    return total

def get_neighbors(solution):
    neighbors = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbor = solution[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def tabu_search(max_iter=100, tabu_size=5):
    current = random.sample(range(len(tasks)), len(tasks))
    best = current[:]
    best_cost = evaluate(best)
    tabu_list = []

    for it in range(max_iter):
        neighbors = get_neighbors(current)
        candidates = [(n, evaluate(n)) for n in neighbors if n not in tabu_list]
        if not candidates:
            break

        candidates.sort(key=lambda x: x[1])
        current, cost = candidates[0]

        if cost < best_cost:
            best, best_cost = current[:], cost
            print(f"[Tabou] Itération {it + 1}: meilleur coût = {best_cost}")

        tabu_list.append(current)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best, best_cost

if __name__ == "__main__":
    sol, cost = tabu_search()
    print(f"✅ Solution finale Tabou : {sol} | Coût = {cost}")
