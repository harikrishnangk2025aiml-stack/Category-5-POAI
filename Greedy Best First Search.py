graph = {
    'Home': ['School', 'Park'],
    'School': ['Hospital'],
    'Park': ['Mall'],
    'Hospital': [],
    'Mall': []
}

h = {
    'Home': 5,
    'School': 2,
    'Park': 4,
    'Hospital': 0,
    'Mall': 3
}

def greedy(start, goal):
    queue = [start]
    visited = []

    while queue:
        queue.sort(key=lambda x: h[x])
        node = queue.pop(0)

        if node == goal:
            print("Goal Reached:", node)
            return

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for i in graph[node]:
                if i not in visited:
                    queue.append(i)

greedy('Home', 'Hospital')