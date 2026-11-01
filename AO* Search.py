graph = {
    'Problem': [['Check Battery', 'Check Power']],
    'Check Battery': [['Replace Battery']],
    'Check Power': [['Repair Wire']],
    'Replace Battery': [],
    'Repair Wire': []
}

cost = {
    'Problem': 0,
    'Check Battery': 2,
    'Check Power': 3,
    'Replace Battery': 2,
    'Repair Wire': 4
}

def ao_star(node):
    if node not in graph or not graph[node]:
        return cost[node], [node]

    best_cost = float('inf')
    best_path = []

    for option in graph[node]:
        total = 0
        path = [node]

        for child in option:
            c, p = ao_star(child)
            total += c
            path += p

        total += cost[node]

        if total < best_cost:
            best_cost = total
            best_path = path

    return best_cost, best_path

result, path = ao_star('Problem')

print("Best Solution:", path)
print("Minimum Cost:", result)